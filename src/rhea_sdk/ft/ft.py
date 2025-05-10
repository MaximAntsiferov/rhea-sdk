from rhea_sdk.ft.commands import FTCommandsBuilder


class FungibleToken:
    def __init__(self, rhea: "Rhea") -> None:
        self._rhea = rhea
        self._commands_builder = self._get_commands_builder()

    def _get_commands_builder(self) -> FTCommandsBuilder:
        return FTCommandsBuilder(
            self._rhea.network_id,
            self._rhea.node_url,
        )

    async def get_metadata(self, token: str) -> str:
        command = self._commands_builder.get_token_metadata(token)
        return await self._rhea.shell.execute_command(command)