from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_admin_mailing = InlineKeyboardButton(text='Рассылка', callback_data='callback_admin_mailing')
kb_admin = InlineKeyboardMarkup()
kb_admin.insert(btn_admin_mailing)