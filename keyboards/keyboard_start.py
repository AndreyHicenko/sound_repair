from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

kb_our_services = InlineKeyboardButton(text='Наши услуги', callback_data='kb_our_services')
kb_kontakt = InlineKeyboardButton(text='Наши контакты', callback_data='kontakt')

kb_start = InlineKeyboardMarkup()
kb_start.insert(kb_our_services)
kb_start.add(kb_kontakt)
