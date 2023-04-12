from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_price_repair = InlineKeyboardButton(text='Прайс-лист на ремонт', callback_data='callback_price_repair')
kb_kontakt = InlineKeyboardButton(text='Наши контакты', callback_data='kontakt')
kb_servise = InlineKeyboardMarkup()
kb_servise.insert(btn_price_repair)
kb_servise.insert(kb_kontakt)