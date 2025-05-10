import subprocess
import tomllib

from rhea_sdk.constances import TESTNET_NETWORK_ID


class ConnectionsConfigManager:

    @classmethod
    def set_connections_config(cls, network_id: str, node_url: str) -> None:
        connections_config = cls.get_connections_config()
        parsed_connections_config = tomllib.loads(connections_config)
        if cls._is_network_id_in_connections_config(network_id, parsed_connections_config):
            cls.edit_connections_config(network_id, node_url)
        else:
            cls.add_connections_config(network_id, node_url)
            cls.remove_unnecessary_fields(network_id)

    @staticmethod
    def _is_network_id_in_connections_config(network_id: str, connections_config: dict) -> bool:
        return "network_connection" in connections_config and network_id in connections_config["network_connection"]

    @staticmethod
    def get_connections_config() -> str:
        result = subprocess.run(["near", "--quiet", "config", "show-connections"], capture_output=True, text=True)
        if result.returncode != 0:
            RuntimeError(result.stderr)
        return "\n".join(result.stderr.splitlines()[2:])

    @staticmethod
    def edit_connections_config(network_id: str, node_url: str) -> None:
        command = ["near", "--quiet", "config", "edit-connection", network_id, "--key", "rpc-api-key", "--value", "null", ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            RuntimeError(result.stderr)

    @classmethod
    def add_connections_config(cls, network_id: str, node_url: str) -> None:
        command = [
            "near", "--quiet", "config", "add-connection",
            "--network-name", network_id,
            "--connection-name", network_id,
            "--rpc-url", node_url,
            "--wallet-url", cls._get_default_wallet_url(network_id),
            "--explorer-transaction-url", cls._get_default_wallet_url(network_id),
            "--rpc-api-key", "None",
            "--linkdrop-account-id", cls._get_default_linkdrop_account_id(network_id),
            "--near-social-db-contract-account-id", cls._get_default_near_social_db_contract_account_id(network_id),
            "--faucet-url", "https://helper.nearprotocol.com/account",
            "--fastnear-url", cls._get_default_fastnear_url(network_id),
            "--staking-pools-factory-account-id", cls._get_default_staking_pools_factory_account_id(network_id),
            "--coingecko-url", "https://api.coingecko.com/",
            "--meta-transaction-relayer-url", "https://near-testnet.api.pagoda.co/relay",
        ]
        result = subprocess.run(command, capture_output=True, text=True, input="No")
        if result.returncode != 0:
            RuntimeError(result.stderr)

    @classmethod
    def remove_unnecessary_fields(cls, network_id: str) -> None:
        for field in ["rpc_api_key", "meta_transaction_relayer_url"]:
            command = ["near", "--quiet", "config", "edit-connection", network_id, "--key", field, "--value", "null"]
            result = subprocess.run(command, capture_output=True, text=True, input="No")
            if result.returncode != 0:
                RuntimeError(result.stderr)


    @staticmethod
    def _get_default_wallet_url(network_id: str) -> str:
        if TESTNET_NETWORK_ID in network_id:
            return "https://testnet.mynearwallet.com/"
        return "https://app.mynearwallet.com/"

    @staticmethod
    def _get_default_explorer_transaction_url(network_id: str) -> str:
        if TESTNET_NETWORK_ID in network_id:
            return "https://explorer.testnet.near.org/transactions/"
        return "https://explorer.near.org/transactions/"

    @staticmethod
    def _get_default_linkdrop_account_id(network_id: str) -> str:
        if TESTNET_NETWORK_ID in network_id:
            return "testnet"
        return "near"

    @staticmethod
    def _get_default_near_social_db_contract_account_id(network_id: str) -> str:
        if TESTNET_NETWORK_ID in network_id:
            return "v1.social08.testnet"
        return "social.near"

    @staticmethod
    def _get_default_fastnear_url(network_id: str) -> str:
        if TESTNET_NETWORK_ID in network_id:
            return "https://test.api.fastnear.com/"
        return "https://api.fastnear.com/"

    @staticmethod
    def _get_default_staking_pools_factory_account_id(network_id: str) -> str:
        if TESTNET_NETWORK_ID in network_id:
            return "pool.f863973.m0"
        return "poolv1.near"
