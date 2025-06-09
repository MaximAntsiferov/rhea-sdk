from rhea_sdk.constances import DEFAULT_MAINNET_RPC_URL
from rhea_sdk.dlc_pool import DLCPool
from rhea_sdk.ft import FungibleToken

from rhea_sdk.account import Account
from rhea_sdk.utils.fastnear import FastNearClient


class Rhea:

    def __init__(
        self,
        account_id: str,
        private_key: str,
        rpc_url: str | list[str] = DEFAULT_MAINNET_RPC_URL,
        storage_auto_deposit: bool = True,
    ) -> None:
        self.rpc_url = rpc_url
        self.storage_auto_deposit = storage_auto_deposit

        self._account = Account(self, account_id, private_key)
        self._ft = FungibleToken(self)
        self._dlc_pool = DLCPool(self)
        self._chain_id = None
        self._fastnear = None
        self._initialized = False

    @property
    def account(self) -> Account:
        self._check_initialized()
        return self._account

    @property
    def ft(self) -> FungibleToken:
        self._check_initialized()
        return self._ft

    @property
    def dlc_pool(self) -> DLCPool:
        self._check_initialized()
        return self._dlc_pool

    @property
    def chain_id(self) -> str:
        self._check_initialized()
        return self._chain_id

    @property
    def fastnear(self) -> FastNearClient:
        self._check_initialized()
        return self._fastnear


    async def startup(self):
        await self._account.startup()
        self._chain_id = self._account.chain_id
        self._fastnear = FastNearClient(self._chain_id)
        self._initialized = True

    def _check_initialized(self):
        if not self._initialized:
            raise RuntimeError("You must call 'startup()' before using this method")
