import asyncio
import json
import locale
import shlex
from json import JSONDecodeError

from rhea_sdk.exceptions import CommandExecutionError


class Shell:

    @staticmethod
    async def execute_command(command: str) -> str | dict:
        process = await asyncio.create_subprocess_exec(
            *shlex.split(command),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        data, error = await process.communicate()
        encoding = locale.getencoding()
        if error:
            raise CommandExecutionError(error.decode(encoding=encoding))
        try:
            return json.loads(data)
        except JSONDecodeError:
            return data.decode(encoding=encoding)
