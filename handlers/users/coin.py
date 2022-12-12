from aiogram import types
from utils import coin_info
from loader import dp


@dp.message_handler()
async def command_price(message: types.Message):
    await coin_info(message)
