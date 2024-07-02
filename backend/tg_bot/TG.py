import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TOKEN


# Запускаем бота и обработчик сообщений
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
        print('Бот запущен')
    except KeyboardInterrupt:
        print('Бот выключен')
