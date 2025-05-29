import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from models import BOT_TOKEN, BASE_DIR

import os

# for i in range(1,24):
#     if (i == 22):
#         break
#     first = str(BASE_DIR / "assets" / "route_4" / f"{i+1}_vladimirskaya-chernyshevskaya.wav")
#     second = str(BASE_DIR / "assets" / "route_4" / f"{i}_vladimirskaya-chernyshevskaya.wav")
#     os.rename(first, second)
#     print(i)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())