import re

from rhea_sdk.account.commands import AccountCommandsBuilder
from rhea_sdk.utils import PublicKeyGenerator


class Account:
    def __init__(
        self,
        rhea: "Rhea",
        account_id: str,
        private_key: str = None,
        seed_phrase: str = None,
    ) -> None:
        self._rhea = rhea
        self.account_id = account_id
        self.private_key = private_key
        self.seed_phrase = seed_phrase
        self.public_key = self._get_public_key(private_key) if private_key else None
        self._commands_builder = self._get_commands_builder()

    def _get_commands_builder(self) -> AccountCommandsBuilder:
        return AccountCommandsBuilder(
            self.account_id,
            self.private_key,
            self.public_key,
            self.seed_phrase,
            self._rhea.network_id,
            self._rhea.node_url,
        )

    @staticmethod
    def _get_public_key(private_key: str) -> str:
        return PublicKeyGenerator.get_from_private_key(private_key)

    async def get_token_balance(self, token: str) -> dict:
        command = self._commands_builder.get_token_balance(token)
        response = await self._rhea.shell.execute_command(command)
        return self._build_token_balance_response(token, response)

    async def get_near_balance(self) -> dict:
        command = self._commands_builder.get_near_balance()
        response = await self._rhea.shell.execute_command(command)
        return self._build_near_balance_response(response)

    async def get_storage_balance(self, contract_id: str) -> str:
        command = self._commands_builder.get_storage_balance(contract_id)
        return await self._rhea.shell.execute_command(command)

    async def deposit_for_storage(self, contract_id: str, amount: float = 0.00125, prepaid_gas: float = 30.0) -> str:
        command = self._commands_builder.deposit_for_storage(contract_id, amount, prepaid_gas)
        return await self._rhea.shell.execute_command(command)


    async def wrap_near(self, amount: float, prepaid_gas: float = 30.0) -> dict:
        command = self._commands_builder.wrap_near(amount, prepaid_gas)
        await self._rhea.shell.execute_command(command)
        return {"wrapped": amount}
        # return self._build_transaction_response(response)

    async def unwrap_near(self, amount: float, prepaid_gas: float = 30.0) -> dict:
        command = self._commands_builder.unwrap_near(amount, prepaid_gas)
        await self._rhea.shell.execute_command(command)
        return {"unwrapped": amount}
        # return self._build_transaction_response(response)

    @staticmethod
    def _build_token_balance_response(token: str, response: str) -> dict:
        match = re.search(r"account has (\d+\.?\d*) ", response)
        return {"token": token, "balance": match.group(1)}

    @staticmethod
    def _build_near_balance_response(response: str) -> dict:
        balance_match = re.search(r"total balance is (\d+\.?\d*) NEAR", response)
        locked_match = re.search(r"but (\d+\.?\d*) NEAR is locked", response)
        return {"token": "near_native", "balance": balance_match.group(1), "locked": locked_match.group(1)}

    # @staticmethod
    # def _build_transaction_response(response: str) -> dict:
    #     gas_pattern = r"Gas burned: (\d+\.\d+)"
    #     fee_pattern = r"Transaction fee: (\d+\.\d+)"
    #     id_pattern = r"Transaction ID: ([A-Za-z0-9]+)"
    #     return {
    #         "gas_burned": float(re.search(gas_pattern, response).group(1)),
    #         "transaction_fee": float(re.search(fee_pattern, response).group(1)),
    #         "transaction_id": re.search(id_pattern, response).group(1)
    #     }