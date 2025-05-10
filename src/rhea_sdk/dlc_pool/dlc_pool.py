import math
from decimal import Decimal
from typing import Iterable

from rhea_sdk.constances import DCL_POOL_FEE_LIST, CONSTANT_D, RHEA_DLC_TESTNET_CONTRACT, TESTNET_NETWORK_ID, \
    RHEA_DLC_MAINNET_CONTRACT
from rhea_sdk.dlc_pool.commands import DLCCommandsBuilder
from rhea_sdk.exceptions import EmptyStorageBalance


class DLCPool:
    def __init__(self, rhea: "Rhea"):
        self._rhea = rhea
        self.dlc_contract_id = self._get_dlc_contract_id(self._rhea.network_id)
        self._commands_builder = self._get_commands_builder()


    def _get_commands_builder(self) -> "DLCCommandsBuilder":
        return DLCCommandsBuilder(
            self._rhea.account.account_id,
            self._rhea.account.private_key,
            self._rhea.account.public_key,
            self._rhea.account.seed_phrase,
            self._rhea.network_id,
            self._rhea.node_url,
            self.dlc_contract_id,
        )

    @staticmethod
    def get_pool_id(token_a: str, token_b: str, fee: int) -> str:
        if fee not in DCL_POOL_FEE_LIST:
            raise ValueError(f"fee must be one of {DCL_POOL_FEE_LIST}")
        return "|".join(sorted([token_a, token_b]) + [str(fee)])

    async def get_pool(self, pool_id: str):
        command = self._commands_builder.get_pool(pool_id)
        return await self._rhea.shell.execute_command(command)

    async def get_pools(self):
        command = self._commands_builder.get_pools()
        return await self._rhea.shell.execute_command(command)

    async def get_tokens_price(self, pool_id: str):
        pool = await self.get_pool(pool_id)
        token_a, token_b, fee = pool_id.split("|")
        return {
            f"{token_a}": math.pow(CONSTANT_D, pool["current_point"] - 1) / (10**18),
            f"{token_b}": math.pow(CONSTANT_D, -pool["current_point"] - 1) * (10**18),
        }

    async def swap(self, token_in: str, token_out: str, pool_id: str, amount: float, min_output_amount: float):
        contracts = (token_in, token_out)
        await self._check_storage_balances(contracts)
        amount = await self._calculate_amount(token_in, amount)
        min_output_amount = await self._calculate_min_output_amount(token_out, min_output_amount)
        command = self._commands_builder.swap(token_in, token_out, pool_id, amount, min_output_amount)
        return await self._rhea.shell.execute_command(command)

    async def _calculate_amount(self,  token_in: str, amount: float) -> str:
        token_in_metadata = await self._rhea.ft.get_metadata(token_in)
        return str(int(Decimal(str(amount)) * 10 ** int(token_in_metadata["decimals"])))

    async def _calculate_min_output_amount(self, token_out: str, min_output_amount: float) -> str:
        token_out_metadata = await self._rhea.ft.get_metadata(token_out)
        return str(int(Decimal(str(min_output_amount)) * 10 ** int(token_out_metadata["decimals"])))

    async def _check_storage_balances(self, contracts_ids: Iterable[str]) -> None:
        for contract_id in contracts_ids:
            if not await self._rhea.account.get_storage_balance(contract_id):
                if self._rhea.storage_auto_deposit:
                    await self._rhea.account.deposit_for_storage(contract_id)
                else:
                    raise EmptyStorageBalance(f"Storage balance deposit for {contract_id} required")

    @staticmethod
    def _get_dlc_contract_id(network_id) -> str:
        return RHEA_DLC_TESTNET_CONTRACT if TESTNET_NETWORK_ID in network_id else RHEA_DLC_MAINNET_CONTRACT