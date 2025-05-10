import json
import shlex
from decimal import Decimal

from rhea_sdk.constances import TESTNET_NETWORK_ID, WRAP_NEAR_TESTNET_CONTRACT, WRAP_NEAR_MAINNET_CONTRACT


class AccountCommandsBuilder:
    def __init__(
        self,
        account_id: str,
        private_key: str,
        public_key: str,
        seed_phrase: str,
        network_id: str,
        node_url: str,
    ):
        self.account_id = account_id
        self.private_key = private_key
        self.public_key = public_key
        self.seed_phrase = seed_phrase
        self.network_id = network_id
        self.node_url = node_url

    def get_token_balance(self, token: str) -> str:
        return f"near --quiet tokens {self.account_id} view-ft-balance {token} network-config {self.network_id} now"

    def get_near_balance(self) -> str:
        return f"near --quiet tokens {self.account_id} view-near-balance network-config {self.network_id} now"

    def get_storage_balance(self, contract_id: str) -> str | None:
        json_args = shlex.quote(json.dumps({"account_id": self.account_id}))
        return f"near --quiet contract call-function as-read-only {contract_id} storage_balance_of json-args {json_args} network-config {self.network_id} now"

    def deposit_for_storage(self, contract_id: str, amount: float, prepaid_gas: float) -> str:
        json_args = "{}"
        if self.private_key:
            return f"near --quiet contract call-function as-transaction {contract_id} storage_deposit json-args {json_args} prepaid-gas '{prepaid_gas} Tgas' attached-deposit '{amount} NEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-plaintext-private-key --signer-public-key {self.public_key} --signer-private-key {self.private_key} send"
        return f"near --quiet contract call-function as-transaction {contract_id} storage_deposit json-args {json_args} prepaid-gas '{prepaid_gas} Tgas' attached-deposit '{amount} NEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-seed-phrase {self.seed_phrase} --seed-phrase-hd-path 'm/44'\''/397'\''/0'\''' send"

    def wrap_near(self, amount: float, prepaid_gas: float) -> str:
        wnear_contract_id = self._get_wnear_contract_id()
        json_args = "{}"
        if self.private_key:
            return f"near --quiet contract call-function as-transaction {wnear_contract_id} near_deposit json-args {json_args} prepaid-gas '{prepaid_gas} Tgas' attached-deposit '{amount} NEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-plaintext-private-key --signer-public-key {self.public_key} --signer-private-key {self.private_key} send"
        return f"near --quiet contract call-function as-transaction {wnear_contract_id} near_deposit json-args {json_args} prepaid-gas '{prepaid_gas} Tgas' attached-deposit '{amount} NEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-seed-phrase {self.seed_phrase} --seed-phrase-hd-path 'm/44'\''/397'\''/0'\''' send"

    def unwrap_near(self, amount: float, prepaid_gas: float = 30.0) -> str:
        wnear_contract_id = self._get_wnear_contract_id()
        amount = str(int(Decimal(str(amount)) * 10**24))
        json_args = shlex.quote(json.dumps({"amount": str(amount)}))
        if self.private_key:
            return f"near --quiet contract call-function as-transaction {wnear_contract_id} near_withdraw json-args {json_args} prepaid-gas '{prepaid_gas} Tgas' attached-deposit '1 yoctoNEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-plaintext-private-key --signer-public-key {self.public_key} --signer-private-key {self.private_key} send"
        return f"near --quiet contract call-function as-transaction {wnear_contract_id} near_withdraw json-args {json_args} prepaid-gas '{prepaid_gas} Tgas' attached-deposit '1 yoctoNEAR' sign-as {self.account_id} network-config {self.network_id} sign-with-seed-phrase {self.seed_phrase} --seed-phrase-hd-path 'm/44'\''/397'\''/0'\''' send"

    def _get_wnear_contract_id(self) -> float:
        if TESTNET_NETWORK_ID in self.network_id:
            return WRAP_NEAR_TESTNET_CONTRACT
        return WRAP_NEAR_MAINNET_CONTRACT
