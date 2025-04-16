import sys
import asyncio
import logging

from constances import WnearUsdcPoolID
from dependencies import get_rhea_dlc_client

logger = logging.getLogger(__name__)

async def main():
    dlc_client = get_rhea_dlc_client()
    pool_info = await dlc_client.get_pool_info(WnearUsdcPoolID.TESTNET.value)
    print(pool_info)
    logger.info(pool_info)

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
asyncio.run(main())
