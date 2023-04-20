from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_price_repair = InlineKeyboardButton(text='Прайс-лист на ремонт', callback_data='callback_price_repair')
btn_example_works = InlineKeyboardButton(text='Примеры наших работ', callback_data='callback_example_works')
kb_kontakt = InlineKeyboardButton(text='Наши контакты', callback_data='kontakt')
kb_servise = InlineKeyboardMarkup()
kb_servise.insert(btn_price_repair)
kb_servise.insert(kb_kontakt)
kb_servise.add(btn_example_works)