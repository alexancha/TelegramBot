from aiogram import types
from loader import dp
from keyboards.default import kb_start
from utils import user_add


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAEGon9jiIHTRZOb2lyXWG7TOv9NS_3mFgACtAoAAnUpUEshSjMe04m96ysE')
    await message.answer('Добро пожаловать!\n'
                        'Здесь ты можешь узнать актуальную информацию'
                        ' о монетах', reply_markup=kb_start)
    await user_add(message)
