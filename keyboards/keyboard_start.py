from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

kb_our_services = InlineKeyboardButton(text='Наши услуги', callback_data='kb_our_services')
kb_kontakt = InlineKeyboardButton(text='Наши контакты', callback_data='kontakt')
btn_example_works = InlineKeyboardButton(text='Примеры наших работ', callback_data='callback_example_works')

kb_start = InlineKeyboardMarkup()
kb_start.insert(kb_our_services)
kb_start.insert(kb_kontakt)
kb_start.add(btn_example_works)
