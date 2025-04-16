import asyncio
import json
import locale
from json import JSONDecodeError

from main import logger
from exceptions import CommandExecutionError


class Executor:
    async def execute_command(self, command: str) -> str | dict:
        pass


class Shell:

    @staticmethod
    async def execute_command(command: str) -> str | dict:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        encoding = locale.getencoding()
        data, error = await process.communicate()
        if error:
            logger.error(error.decode(encoding))
            raise CommandExecutionError(process.stderr)
        try:
            result = json.loads(data)
        except JSONDecodeError as e:
            logger.error(e)
            raise
        return result
