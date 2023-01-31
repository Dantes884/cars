from aiogram import executor

from addons.command_cars import show_cars
from addons.db import create_table, init
from config import dp


async def startup(_):
    """
        запускаем дополнительные сторонние сервисы
    """
    init()
    create_table()


dp.register_message_handler(show_cars, commands=['cars'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)