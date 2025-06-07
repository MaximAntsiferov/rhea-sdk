from rhea_sdk.constances import TESTNET_CHAIN_ID, WRAP_NEAR_TESTNET_CONTRACT, WRAP_NEAR_MAINNET_CONTRACT


class FungibleToken:
    def __init__(self, rhea: "Rhea") -> None:
        self._rhea = rhea

    @property
    def wnear_contract(self) -> str:
        if self._rhea.chain_id == TESTNET_CHAIN_ID:
            return WRAP_NEAR_TESTNET_CONTRACT
        return WRAP_NEAR_MAINNET_CONTRACT


    async def get_metadata(self, contract_id: str) -> dict:
        result = await self._rhea.account._acc.view_function(contract_id, "ft_metadata", {})
        return result.result
