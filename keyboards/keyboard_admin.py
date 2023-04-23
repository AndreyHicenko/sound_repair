from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

btn_admin_mailing = InlineKeyboardButton(text='Рассылка', callback_data='callback_admin_mailing')
kb_admin = InlineKeyboardMarkup()
kb_admin.insert(btn_admin_mailing)

kb_admin_mail_back = InlineKeyboardButton(text='Назад', callback_data='callback_admin_mail_back')
kb_admin_mailing_only_back = InlineKeyboardMarkup()
kb_admin_mailing_only_back.insert(kb_admin_mail_back)

kb_admin_mail_message_accept = InlineKeyboardButton(text='Отправить',
                                                    callback_data='callback_admin_mail_message_accept')
kb_admin_mail_message_cancel = InlineKeyboardButton(text='Отменить отправку',
                                                    callback_data='callback_admin_mail_message_cancel')
kb_admin_mailing = InlineKeyboardMarkup()
kb_admin_mailing.insert(kb_admin_mail_message_accept)
kb_admin_mailing.add(kb_admin_mail_message_cancel)

btn_admin_mailing_send_back = InlineKeyboardButton(text='Перейти в консоль администратора',
                                                   callback_data='callback_admin_mail_back_to_console')
kb_admin_mailing_send_back = InlineKeyboardMarkup()
kb_admin_mailing_send_back.add(btn_admin_mailing_send_back)
