from aiogram import types
from loader import dp


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer('Введи название монеты для просмотра информации о ней\n'
                         'Нажми /top10 для просмотра топ10 монет по капитализации\n'
                         'Раз в неделю бот будет предлагать пару монет к рассмотрению\n'
                         'Нажми /2coins для просмотра пары монет сейчас\n'
                         'Нажми /estimate для оценка бота!')