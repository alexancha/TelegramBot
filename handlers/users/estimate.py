from aiogram import types
from loader import dp, bot
from keyboards.inline import inline_kb1

@dp.message_handler(commands=['estimate'])
async def command_estimate(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пожалуйста, оцени бота', reply_markup=inline_kb1)


@dp.callback_query_handler(text='button')
async def process_callback_estimate(call: types.CallbackQuery):
    await call.answer('Спасибо')