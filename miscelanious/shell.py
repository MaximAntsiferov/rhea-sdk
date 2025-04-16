import json
import locale
import shlex

import asyncio
class Shell:
    @staticmethod
    async def execute_command(command: str) -> str | dict:
        process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout_data = await process.stdout.read()
        stderr_data = await process.stderr.read()
        encoding = locale.getencoding()
        print(encoding)
        await process.wait()
        print(f"Output: {stdout_data.decode(encoding)}")
        print(f"Errors: {stderr_data.decode(encoding)}")
shell = Shell()
pool_id = "usdc.fakes.testnet|wrap.testnet|100"
z = shlex.quote(json.dumps({"pool_id": pool_id}))
swap = f"near --quiet contract call-function as-read-only dclv2.ref-dev.testnet get_pool json-args {z} network-config testnet now"
async def main():
    await shell.execute_command(swap)
asyncio.run(main())
