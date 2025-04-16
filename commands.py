import json
import shlex

from constances import NetworkID, DLCContract


class CommandsBuilder:

    def get_pool_info(self, pool_id: str, network_id: NetworkID) -> str:
        json_args = shlex.quote(json.dumps({"pool_id": pool_id}))
        return f"near --quiet contract call-function as-read-only dclv2.ref-dev.testnet get_pool json-args {json_args} network-config {network_id} now"

    def swap(self, token_in: str, token_out: str, pool_id: str, amount: float, network_id: NetworkID, min_output_amount) -> str:
        msg = shlex.quote(json.dumps({
            "Swap": {
                "pool_ids": [pool_id],
                "output_token": token_out,
                "min_output_amount": min_output_amount,
            }
        }))

        json_args = shlex.quote(json.dumps({
            "receiver_id": self._get_swap_receiver_id(network_id),
            "amount": self._get_swap_amount(amount),
            "msg": msg,
        }))

        return f"near --quiet contract call-function as-transaction {token_in} ft_transfer_call json-args {json_args} prepaid-gas '100.0 Tgas' attached-deposit '1 yoctoNEAR' sign-as max-test.testnet network-config {network_id} sign-with-legacy-keychain send"

    @staticmethod
    def _get_swap_receiver_id(network_id: NetworkID) -> DLCContract:
        return DLCContract.TESTNET if network_id.value == "testnet" else DLCContract.MAINNET

    @staticmethod
    def _get_swap_amount(amount: float) -> float:
        return amount * 100000000000000000000000
