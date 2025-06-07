from decimal import Decimal

from py_near import account

from rhea_sdk.constances import NEAR, ONE_YOCTO_NEAR,  FT_MINIMUM_STORAGE_BALANCE


class Account:
    def __init__(
        self,
        rhea: "Rhea",
        account_id: str,
        private_key: str = None,
    ) -> None:
        self._rhea = rhea
        self.account_id = account_id
        self.private_key = private_key
        self._acc = account.Account(self.account_id, self.private_key, self._rhea.rpc_url)
        self.chain_id = None

    async def startup(self) -> None:
        await self._acc.startup()
        self.chain_id = self._acc.chain_id


    async def get_token_balance(self, token: str) -> str:
        data = await self._rhea.fastnear.get_full_account_data(self.account_id)
        if not data.get("tokens"):
            raise ValueError(f"No tokens available for account {self.account_id}")
        for token_ in data["tokens"]:
            if token_["contract_id"] == token:
                token_metadata = await self._rhea.ft.get_metadata(token)
                return str(Decimal(token_["balance"]) / 10 ** token_metadata["decimals"])
        return "0"


    async def get_near_balance(self) -> str:
        data = await self._rhea.fastnear.get_full_account_data(self.account_id)
        if not data.get("state"):
            raise ValueError(f"No state available for account {self.account_id}")
        return str(Decimal(data["state"]["balance"]) / NEAR)


    async def get_storage_balance(self, contract_id: str) -> dict:
        result =  await self._acc.view_function(
            contract_id,
            "storage_balance_of",
            {"account_id": self.account_id},
        )
        return result.result


    async def deposit_for_storage(self, contract_id: str, amount: str = FT_MINIMUM_STORAGE_BALANCE) -> None:
        converted_amount = int(Decimal(amount) * Decimal(NEAR))
        await self._acc.function_call(contract_id, "storage_deposit", {}, amount=converted_amount)


    async def wrap_near(self, amount: str) -> str:
        converted_amount = int(Decimal(amount) * Decimal(NEAR))
        await self._acc.function_call(
            self._rhea.ft.wnear_contract,
            "near_deposit",
            {},
            amount=converted_amount,
        )
        return amount

    async def unwrap_near(self, amount: str) -> str:
        converted_amount = str(int(Decimal(amount) * Decimal(NEAR)))
        await self._acc.function_call(
            self._rhea.ft.wnear_contract,
            "near_withdraw",
            {"amount": converted_amount},
            amount=1,
        )
        return amount
