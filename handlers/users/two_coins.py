from aiogram import types
from loader import dp
from utils import two_coins


@dp.message_handler(commands=['2coins'])
async def command_two_coins(message: types.Message):
    await two_coins(message)
