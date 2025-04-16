from functools import lru_cache

from commands import CommandsBuilder
from constances import NodeURL, NetworkID
from rhea_dlc_client import DCLClient
from shell import Executor, Shell

@lru_cache(maxsize=1)
def get_shell_executor() -> Shell:
    return Shell()

@lru_cache(maxsize=1)
def get_commands_builder() -> CommandsBuilder:
    return CommandsBuilder()


@lru_cache(maxsize=1)
def get_rhea_dlc_client(
    node_url: str = NodeURL.TESTNET.value,
    network_id: NetworkID = NetworkID.TESTNET,
    account_id: str,
    private_key: str,
    executor: Executor = get_shell_executor(),
    commands_builder: CommandsBuilder = get_commands_builder(),
) -> DCLClient:
    return DCLClient(
        node_url=node_url,
        network_id=network_id,
        executor=executor,
        commands_builder=commands_builder,
    )
