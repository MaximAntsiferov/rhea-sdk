from rhea_sdk.constances import TESTNET_NETWORK_ID, DEFAULT_TESTNET_NODE_URL, DEFAULT_MAINNET_NODE_URL, MAINNET_NETWORK_ID
from rhea_sdk.dlc_pool import DLCPool
from rhea_sdk.ft import FungibleToken
from rhea_sdk.shell import Shell
from rhea_sdk.account import Account
from rhea_sdk.utils import ConnectionsConfigManager


class Rhea:
    """A NEAR protocol account interface for interacting with the blockchain.

        Args:
            account_id: NEAR account identifier (e.g. example.near)
            network_id: 'mainnet' or 'testnet' (default: testnet)
            private_key: Account private key (either this or seed_phrase required)
            seed_phrase: Account seed phrase (either this or private_key required)
            node_url: Custom RPC node URL (optional)
    """
    def __init__(
        self,
        account_id: str,
        network_id: str = TESTNET_NETWORK_ID,
        private_key: str = None,
        seed_phrase: str = None,
        node_url: str = None,
        storage_auto_deposit: bool = True,
    ) -> None:

        if not private_key and not seed_phrase:
            raise ValueError("You should provide either private_key or seed_phrase")

        self.network_id = self._set_network_id(network_id)
        self.node_url = self._set_node_url(node_url)
        self.shell = Shell()
        self.storage_auto_deposit = storage_auto_deposit

        self.account = Account(self, account_id, private_key, seed_phrase)
        self.ft = FungibleToken(self)
        self.dlc_pool = DLCPool(self)


    @staticmethod
    def _set_network_id(network_id: str) -> str:
        if network_id not in [MAINNET_NETWORK_ID, TESTNET_NETWORK_ID]:
            raise ValueError(f"'network_id' must be either '{MAINNET_NETWORK_ID}' or '{TESTNET_NETWORK_ID}'")
        return f"rhea_{network_id}"

    def _set_node_url(self, node_url: str | None) -> str:
        node_url = node_url or self._get_default_node_url()
        self._set_connection_config(node_url)
        return node_url

    def _get_default_node_url(self) -> str:
        if TESTNET_NETWORK_ID in self.network_id:
            return DEFAULT_TESTNET_NODE_URL
        return DEFAULT_MAINNET_NODE_URL

    def _set_connection_config(self, node_url: str) -> None:
        ConnectionsConfigManager.set_connections_config(self.network_id, node_url)
