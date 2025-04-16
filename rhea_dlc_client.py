import logging

from commands import CommandsBuilder
from constances import NetworkID
from shell import Executor


logger = logging.getLogger(__name__)

class DCLClient:

    def __init__(
            self,
            node_url: str,
            network_id: NetworkID,
            executor: Executor,
            commands_builder: CommandsBuilder,
    ):
        self.node_url = node_url
        self.network_id = network_id
        self.executor = executor
        self.commands_builder = commands_builder


    async def get_pool_info(self, pool_id: str) -> dict:
        command = self.commands_builder.get_pool_info(pool_id, self.network_id)
        return await self.executor.execute_command(command)

    async def get_current_price(self, pool_id: str):
        pool_info = await self.get_pool_info(pool_id)
        current_price = 1.0001 ** -pool_info["current_point"] * 1000000000000000000
        or_current_price = 1 / current_price
        logger.debug(current_price)
        logger.debug(or_current_price)
        return current_price

    async def swap(self, pool_id: str) -> dict:
        command = self.commands_builder.get_pool_info(pool_id, self.network_id)
        return await self.executor.execute_command(command)
