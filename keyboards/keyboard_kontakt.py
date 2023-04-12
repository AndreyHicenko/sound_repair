from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

kb_back_to_servises = InlineKeyboardButton(text='Вернуться к услугам', callback_data='kb_our_services')
kb_call = InlineKeyboardButton(text='Позвонить нам', url='http://onmap.uz/tel/79515583318')
kb_kontakt = InlineKeyboardMarkup()
kb_kontakt.add(kb_call)
kb_kontakt.add(kb_back_to_servises)
