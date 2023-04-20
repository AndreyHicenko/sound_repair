from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


btn_photo_back = InlineKeyboardButton(text='⬅', callback_data='callback_photo_back')
btn_photo_forward = InlineKeyboardButton(text='➡', callback_data='callback_photo_forward')
kb_back_to_servises = InlineKeyboardButton(text='Вернуться к услугам', callback_data='kb_our_services')
kb_photo_example_works = InlineKeyboardMarkup()
kb_photo_example_works.insert(btn_photo_back)
kb_photo_example_works.insert(btn_photo_forward)
kb_photo_example_works.add(kb_back_to_servises)
