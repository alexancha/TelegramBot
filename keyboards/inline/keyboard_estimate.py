from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji

inline_btn_1 = InlineKeyboardButton(emoji.emojize(':thumbs_up:'), callback_data='button')
inline_btn_2 = InlineKeyboardButton(emoji.emojize(':thumbs_down:'), callback_data='button')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).insert(inline_btn_2)
