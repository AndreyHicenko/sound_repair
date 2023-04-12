from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_price_repair_din = InlineKeyboardButton(text='Динамики', callback_data='kb_price_repair_dinamic')
btn_price_repair_sub = InlineKeyboardButton(text='Сабвуферы', callback_data='kb_price_repair_sub')
btn_price_repair_amplifier = InlineKeyboardButton(text='Усилители', callback_data='kb_price_repair_amplifier')
kb_back_to_servises = InlineKeyboardButton(text='Вернуться к услугам', callback_data='kb_our_services')
kb_price_repair = InlineKeyboardMarkup()
kb_price_repair.insert(btn_price_repair_din)
kb_price_repair.insert(btn_price_repair_sub)
kb_price_repair.insert(btn_price_repair_amplifier)
kb_price_repair.add(kb_back_to_servises)

kb_price_repair_din_back = InlineKeyboardButton(text='Вернуться к прайс листам',
                                                callback_data='callback_price_repair')
kb_price_repair_din_replay = InlineKeyboardButton(text='Вернуться к услугам', callback_data='kb_our_services')
kb_price_repair_din_markup = InlineKeyboardMarkup()
kb_price_repair_din_markup.insert(kb_price_repair_din_back)
kb_price_repair_din_markup.add(kb_price_repair_din_replay)
