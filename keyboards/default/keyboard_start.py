from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji

b1 = KeyboardButton('/help') #кнопки
b2 = KeyboardButton('/top10')
b3 = KeyboardButton('/estimate')
b4 = KeyboardButton('/2coins')

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start.add(b1).insert(b2).add(b3).insert(b4)
