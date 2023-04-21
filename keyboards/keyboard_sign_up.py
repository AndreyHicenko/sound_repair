from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_sign_up_installation = InlineKeyboardButton(text='Записаться на установку акустики',
                                                callback_data='callback_installation')
btn_sign_up_car_service = InlineKeyboardButton(text='Записаться в автосервис', callback_data='callback_car_service')
btn_sign_up_acoustics_repair = InlineKeyboardButton(text='Записаться на ремонт акустики',
                                                    callback_data='callback_acoustics_repair')
kb_back_to_servises = InlineKeyboardButton(text='Вернуться к услугам', callback_data='kb_our_services')
kb_sign_up = InlineKeyboardMarkup()
kb_sign_up.insert(btn_sign_up_installation)
kb_sign_up.add(btn_sign_up_car_service)
kb_sign_up.add(btn_sign_up_acoustics_repair)
kb_sign_up.add(kb_back_to_servises)

btn_sign_up_installation_yes = InlineKeyboardButton(text='Да', callback_data='callback_installation_yes')
btn_sign_up_installation_no = InlineKeyboardButton(text='Нет', callback_data='callback_installation_no')
kb_sign_up_name = InlineKeyboardMarkup()
kb_sign_up_name.insert(btn_sign_up_installation_yes)
kb_sign_up_name.insert(btn_sign_up_installation_no)

btn_sign_up_installation_num_yes = InlineKeyboardButton(text='Да',
                                                        callback_data='callback_sign_up_installation_num_yes')
btn_sign_up_installation_num_no = InlineKeyboardButton(text='Нет', callback_data='callback_sign_up_installation_num_no')
kb_sign_up_num = InlineKeyboardMarkup()
kb_sign_up_num.insert(btn_sign_up_installation_num_yes)
kb_sign_up_num.insert(btn_sign_up_installation_num_no)

btn_sign_up_only_back_num = InlineKeyboardButton(text='Назад', callback_data='callback_sign_up_back_num')
kb_sign_up_only_back_num = InlineKeyboardMarkup()
kb_sign_up_only_back_num.insert(btn_sign_up_only_back_num)


btn_sign_up_only_back = InlineKeyboardButton(text='Назад', callback_data='callback_sign_up_back')
kb_sign_up_only_back = InlineKeyboardMarkup()
kb_sign_up_only_back.insert(btn_sign_up_only_back)

kb_back_to_servises = InlineKeyboardButton(text='Вернуться к услугам', callback_data='kb_our_services')
kb_sign_up_back_to_servis = InlineKeyboardMarkup()
kb_sign_up_back_to_servis.insert(kb_back_to_servises)
