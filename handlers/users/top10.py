from aiogram import types
from utils import top10
from loader import dp

@dp.message_handler(commands=['top10'])
async def command_top10(message: types.Message):
    await top10(message)
