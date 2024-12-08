import asyncio
import logging

from bot_config import dp, bot
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router

async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
