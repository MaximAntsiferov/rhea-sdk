import json
import shlex


class DLCCommandsBuilder:

    def __init__(
        self,
        account_id: str,
        private_key: str,
        public_key: str,
        seed_phrase: str,
        network_id: str,
        node_url: str,
        dlc_contract_id: str
    ):
        self.account_id = account_id
        self.private_key = private_key
        self.public_key = public_key
        self.seed_phrase = seed_phrase
        self.network_id = network_id
        self.node_url = node_url
        self.dlc_contract_id = dlc_contract_id

    def get_pools(self) -> str:
        json_args = shlex.quote("{}")
        return f"near --quiet contract call-function as-read-only {self.dlc_contract_id} list_pools json-args {json_args} network-config {self.network_id} now"

    @staticmethod
    def get_pool_id(token_a: str, token_b: str, fee: int) -> str:
        return "|".join(sorted([token_a, token_b]) + [str(fee)])

    def get_pool(self, pool_id: str) -> str:
        json_args = shlex.quote(json.dumps({"pool_id": pool_id}))
        return f"near --quiet contract call-function as-read-only {self.dlc_contract_id} get_pool json-args {json_args} network-config {self.network_id} now"

    def swap(self, token_in: str, token_out: str, pool_id: str, amount: str, min_output_amount: str) -> str:
        msg = json.dumps({
            "Swap": {
                "pool_ids": [pool_id],
                "output_token": token_out,
                "min_output_amount": min_output_amount,
            }
        })

        json_args = shlex.quote(json.dumps({
            "receiver_id": self.dlc_contract_id,
            "amount": amount,
            "msg": msg,
        }))
        if self.private_key:
            return f"near --quiet contract call-function as-transaction {token_in} ft_transfer_call json-args {json_args} prepaid-gas '100.0 Tgas' attached-deposit '1 yoctoNEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-plaintext-private-key --signer-public-key {self.public_key} --signer-private-key {self.private_key} send"
        return f"near --quiet contract call-function as-transaction {token_in} ft_transfer_call json-args {json_args} prepaid-gas '100.0 Tgas' attached-deposit '1 yoctoNEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-seed-phrase {self.seed_phrase} --seed-phrase-hd-path 'm/44'\''/397'\''/0'\''' send"