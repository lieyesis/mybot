import asyncio
import logging
from bot_config import  dp,bot, database
import handlers


async def on_startup(_):
    database.create_tables()

async def main():
    dp.include_router(handlers.start_router)
    dp.include_router(handlers.admin_router)
    dp.include_router(handlers.review_router)
    dp.include_router(handlers.menu_router)
    dp.include_router(handlers.random_meal_router)
    dp.include_router(handlers.echo_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())