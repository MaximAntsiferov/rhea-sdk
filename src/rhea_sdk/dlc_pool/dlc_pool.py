import json
import math
import re
from decimal import Decimal
from typing import Iterable

from py_near.models import TransactionResult
from rhea_sdk.constances import DCL_POOL_FEE_LIST, CONSTANT_D, RHEA_DLC_TESTNET_CONTRACT, TESTNET_CHAIN_ID, \
    RHEA_DLC_MAINNET_CONTRACT, NEAR
from rhea_sdk.exceptions import EmptyStorageBalance, TransactionError, TransactionReceiptError


class DLCPool:
    def __init__(self, rhea: "Rhea"):
        self._rhea = rhea

    @property
    def dlc_contract_id(self) -> str:
        if self._rhea.chain_id == TESTNET_CHAIN_ID:
            return RHEA_DLC_TESTNET_CONTRACT
        return RHEA_DLC_MAINNET_CONTRACT


    @staticmethod
    def get_pool_id(token_a: str, token_b: str, fee: int) -> str:
        if fee not in DCL_POOL_FEE_LIST:
            raise ValueError(f"fee must be one of {DCL_POOL_FEE_LIST}")
        return "|".join(sorted([token_a, token_b]) + [str(fee)])

    async def get_pool(self, pool_id: str) -> dict:
        result = await self._rhea.account._acc.view_function(self.dlc_contract_id, "get_pool", {"pool_id": pool_id})
        return result.result

    async def get_pools(self) -> list[dict]:
        result = await self._rhea.account._acc.view_function(self.dlc_contract_id, "list_pools", {})
        return result.result

    async def get_tokens_price(self, pool_id: str) -> dict[str, str]:
        pool = await self.get_pool(pool_id)
        token_a, token_b, fee = pool_id.split("|")
        return {
            token_a: str(math.pow(CONSTANT_D, pool["current_point"] - 1) / (10**18)),
            token_b: str(math.pow(CONSTANT_D, -pool["current_point"] - 1) * (10**18)),
        }

    async def swap(self, token_in: str, token_out: str, pool_id: str, amount: str, min_output_amount: str) -> TransactionResult:
        contracts = (token_in, token_out)
        await self._check_storage_balances(contracts)
        amount = await self._calculate_amount(token_in, amount)
        min_output_amount = await self._calculate_min_output_amount(token_out, min_output_amount)
        msg = json.dumps({
            "Swap": {
                "pool_ids": [pool_id],
                "output_token": token_out,
                "min_output_amount": min_output_amount,
            }
        })

        json_args = {
            "receiver_id": self.dlc_contract_id,
            "amount": amount,
            "msg": msg,
        }
        result = await self._rhea.account._acc.function_call(token_in, "ft_transfer_call", json_args, amount=1)
        if result.status.get("Failure"):
            raise TransactionError(result.status)
        if token_out == self._rhea.ft.wrap_contract:
            amount_out = self._get_amount_out(result) / NEAR
            await self._rhea.account.wrap_near(amount_out)
        return result

    async def _calculate_amount(self,  token_in: str, amount: str) -> str:
        token_in_metadata = await self._rhea.ft.get_metadata(token_in)
        return str(int(Decimal(amount) * 10 ** int(token_in_metadata["decimals"])))

    async def _calculate_min_output_amount(self, token_out: str, min_output_amount: str) -> str:
        token_out_metadata = await self._rhea.ft.get_metadata(token_out)
        return str(int(Decimal(min_output_amount) * 10 ** int(token_out_metadata["decimals"])))

    async def _check_storage_balances(self, contracts_ids: Iterable[str]) -> None:
        for contract_id in contracts_ids:
            if not await self._rhea.account.get_storage_balance(contract_id):
                if self._rhea.storage_auto_deposit:
                    await self._rhea.account.deposit_for_storage(contract_id)
                else:
                    raise EmptyStorageBalance(f"Storage balance deposit for {contract_id} required")

    @staticmethod
    def _get_amount_out(transaction_result: TransactionResult):
        match = re.search(r'"amount_out":"(\d+)"', transaction_result.receipt_outcome[1].logs[0])
        if match:
            return match.group(1)
        raise TransactionReceiptError("Error while getting transaction amount_out")
