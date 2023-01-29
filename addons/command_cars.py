from aiogram import types
from addons.db import get_data
from time import sleep


async def show_cars(message: types.Message):
    """
        Функция покажет пользователю команды
    """
    i = 0
    for i in range(len(get_data())):
        car = get_data()[i]

        await message.answer(text=f'''
Марка - {car[1]} 
Цена - {car[2]}
Информация - {car[3]}
Ссылка - {car[4]}
''')
        sleep(3)
    await message.delete()