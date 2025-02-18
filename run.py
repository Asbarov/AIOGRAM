import asyncio 
from aiogram import Dispatcher,Bot
from config import TOKEN
from handlers import rt
from models import async_main

async def main():
    await async_main()
    bot=Bot(token=TOKEN)
    dp=Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())

