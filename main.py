from aiogram import Bot, Dispatcher, types
import asyncio
from config import TOKEN
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from keyboards.keyboard_start import *
from keyboards.keyboard_servises import *
from keyboards.keyboard_kontakt import *
from keyboards.keyboard_price_lists import *
from keyboards.keyboard_admin import *
from datebase.query_datebase import *
from keyboards.keyboard_photo_example_works import *
from keyboards.keyboard_sign_up import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class Mydialog(StatesGroup):
    state_sign_up_mobile_number_car_service = State()
    state_sign_up_name_car_service = State()
    otvet = State()
    state_sign_up_name = State()
    state_sign_up_mobile_number = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    # админ панель начало
    admin_list_id = []
    for i in range(len((await search_admin_users()))):
        admin_list_id.append(int((await (search_admin_users()))[i]['id_admin_users']))
    if message.from_user.id in admin_list_id:
        await message.answer("<b>Здравствуйте!</b> Вас приветствует консоль администратора<b>"
                             " бота студии автозвука SOUND REPAIR.</b>",
                             parse_mode="HTML", reply_markup=kb_admin)
    else:
        list_users_id = [int(s['id_users']) for s in (await search_users_id())]
        if message.from_user.id not in list_users_id:
            (await add_users_id(message.from_user.id))
        await message.answer("<b>Здравствуйте!</b> Вас приветствует<b>"
                             " бот студии автозвука SOUND REPAIR.</b>",
                             parse_mode="HTML", reply_markup=kb_start)


# консоль администратора
@dp.callback_query_handler(text='callback_admin_mailing')
async def callback_admin_mailing(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 'Введите текст рассылки', reply_markup=kb_admin_mailing_only_back)
    await Mydialog.otvet.set()


@dp.callback_query_handler(text='callback_admin_mail_back', state=Mydialog.otvet)
async def callback_admin_mailing_back_only(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    admin_list_id = []
    for i in range(len((await search_admin_users()))):
        admin_list_id.append(int((await (search_admin_users()))[i]['id_admin_users']))
    if callback.from_user.id in admin_list_id:
        await bot.send_message(callback.from_user.id, "Вы находитесь в консоли администратора<b>"
                                                      " бота студии автозвука SOUND REPAIR.</b>",
                               parse_mode="HTML", reply_markup=kb_admin)


@dp.callback_query_handler(text='callback_admin_mail_back_to_console')
async def callback_admin_mailing_back(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    admin_list_id = []
    for i in range(len((await search_admin_users()))):
        admin_list_id.append(int((await (search_admin_users()))[i]['id_admin_users']))
    if callback.from_user.id in admin_list_id:
        await bot.send_message(callback.from_user.id, "Вы находитесь в консоли администратора<b>"
                                                      " бота студии автозвука SOUND REPAIR.</b>",
                               parse_mode="HTML", reply_markup=kb_admin)


@dp.callback_query_handler(text='callback_admin_mail_message_accept', state=Mydialog.otvet)
async def callback_admin_mailing_accept(callback: types.callback_query, state: FSMContext):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    admin_list_id = []
    for i in range(len((await search_admin_users()))):
        admin_list_id.append(int((await (search_admin_users()))[i]['id_admin_users']))
    for s in (await search_users_id()):
        if int(s['id_users']) not in admin_list_id:
            await bot.send_message(int(s['id_users']), (await get_admin_lost_message(callback.from_user.id)))
    try:
        await bot.send_message(callback.from_user.id, "Отлично! Ваше сообщение доставлено",
                               reply_markup=kb_admin_mailing_send_back)
        await state.finish()
    except Exception:
        await bot.send_message(callback.from_user.id, "Что-то пошло не так", reply_markup=kb_admin_mailing_send_back)
        await state.finish()


@dp.message_handler(state=Mydialog.otvet)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        (await update_lost_message_admin(user_message, message.from_user.id))
        await Mydialog.otvet.set()
        await message.answer(f"❓ <b>Вы действительно хотите совершить рассылку со следующим содержимым?</b>\n\n\n"
                             f"{user_message}", parse_mode='HTML', reply_markup=kb_admin_mailing)


@dp.callback_query_handler(text='callback_admin_mail_message_cancel', state=Mydialog.otvet)
async def callback_admin_mail_message_cancel(callback: types.callback_query, state: FSMContext):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "Отправка отменена",
                           parse_mode="HTML", reply_markup=kb_admin_mailing_send_back)
    await state.finish()


# рядовый пользовательский контекст
@dp.callback_query_handler(text='kb_our_services')
async def our_services_callback(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "<b>Наши услуги</b>\n \n"
                                                  "👻Продажа автозвука по низким ценам;\n \n"
                                                  "😱Гарантия на месте от оф.центра;\n \n"
                                                  "🍒Установка автозвука и автоэлектрики любой сложности;\n \n"
                                                  "🔧Ремонт динамиков и звукоусиливающей аппаратуры \n \n"
                                                  "👍На все выполненные работы предоставляются чеки, бумаги, акт проделанных работ.",
                           parse_mode="HTML", reply_markup=kb_servise)


# колбек на кнопку прайс листа на ремонт
@dp.callback_query_handler(text='callback_price_repair')
async def price_repair_callback(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, 'Прайс лист на ремонт какой категории вас интересует?',
                           reply_markup=kb_price_repair)


@dp.callback_query_handler(text='kontakt')
async def kontakt_callback(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, "<b>🏢 Мы находимся по адресу:</b> \n"
                                                  "Площадь Октябрьская 76Г (ТЦ Автодом 2й этаж), Россошь\n"
                                                  "<b>🕐 Мы работаем по графику:</b>\n"
                                                  "<b>Пн</b> 10:00 - 18:00\n"
                                                  "<b>Вт</b> 10:00 - 18:00\n"
                                                  "<b>Ср</b> 10:00 - 18:00\n"
                                                  "<b>Чт</b> 10:00 - 18:00\n"
                                                  "<b>Пт</b> 10:00 - 18:00\n"
                                                  "<b>Сб</b> 10:00 - 18:00\n"
                                                  "<b>Вс</b> 10:00 - 18:00",
                           parse_mode="HTML", reply_markup=kb_kontakt)


@dp.callback_query_handler(text='kb_price_repair_dinamic')
async def kb_price_repair_dinamic(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    price_dinamic = (await search_db_price_din())
    await bot.send_message(callback.from_user.id,
                           f"❗ <b>Все цены указаны с запчастью</b> \n\n"
                           f"💵{price_dinamic[0]['type_work']} - <b>от"
                           f" {price_dinamic[0]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[1]['type_work']} - <b>от"
                           f" {price_dinamic[1]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[2]['type_work']} - <b>от"
                           f" {price_dinamic[2]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[3]['type_work']} - <b>от"
                           f" {price_dinamic[3]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[4]['type_work']} - <b>от"
                           f" {price_dinamic[4]['price']} Руб. </b>\n\n\n"
                           f"💵{price_dinamic[5]['type_work']} - <b>от"
                           f" {price_dinamic[5]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[6]['type_work']} - <b>от"
                           f" {price_dinamic[6]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[7]['type_work']} - <b>от"
                           f" {price_dinamic[7]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[8]['type_work']} - <b>от"
                           f" {price_dinamic[8]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[9]['type_work']} - <b>от"
                           f" {price_dinamic[9]['price']} Руб. </b>\n\n"
                           f"💵{price_dinamic[10]['type_work']} - <b>от"
                           f" {price_dinamic[10]['price']} Руб. </b>\n\n"
                           , parse_mode="HTML",
                           reply_markup=kb_price_repair_din_markup)


@dp.callback_query_handler(text='kb_price_repair_sub')
async def kb_price_repair_subwoofer(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    price_subwoofer = (await search_db_price_sub())
    await bot.send_message(callback.from_user.id,
                           f"❗ <b>Цена ремонта указана без запчасти</b> \n\n"
                           f"💵{price_subwoofer[0]['type_work']}\n- <b>от "
                           f"{price_subwoofer[0]['price']} Руб.</b> \n\n"
                           f"💵{price_subwoofer[1]['type_work']}\n- <b>от "
                           f"{price_subwoofer[1]['price']} Руб.</b> \n\n"
                           f"💵{price_subwoofer[2]['type_work']}\n- <b>от "
                           f"{price_subwoofer[2]['price']} Руб.</b> \n\n"
                           f"💵{price_subwoofer[3]['type_work']}\n- <b>от "
                           f"{price_subwoofer[3]['price']} Руб.</b> \n\n"
                           f"💵{price_subwoofer[4]['type_work']}\n- <b>от "
                           f"{price_subwoofer[4]['price']} Руб.</b> \n\n"
                           f"💵{price_subwoofer[5]['type_work']}\n- <b>от "
                           f"{price_subwoofer[5]['price']} Руб.</b> \n\n"
                           f"❗ <b>Цену запчастей уточняете у мастера лично или на сайте Ремдинамик.ру</b>",
                           parse_mode='HTML',
                           reply_markup=kb_price_repair_din_markup
                           )


@dp.callback_query_handler(text='kb_price_repair_amplifier')
async def kb_price_repair_subwoofer(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    price_amplifier = (await search_db_price_amplifier())
    await bot.send_message(callback.from_user.id,
                           f"❗ <b>Все цены указаны с запчастью</b> \n\n"
                           f"💵{price_amplifier[0]['type_work']}\n - <b>от"
                           f" {price_amplifier[0]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[1]['type_work']}\n - <b>от"
                           f" {price_amplifier[1]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[2]['type_work']}\n - <b>от"
                           f" {price_amplifier[2]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[3]['type_work']}\n - <b>от"
                           f" {price_amplifier[3]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[4]['type_work']}\n - <b>от"
                           f" {price_amplifier[4]['price']} Руб. </b>\n\n\n"
                           f"💵{price_amplifier[5]['type_work']}\n - <b>от"
                           f" {price_amplifier[5]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[6]['type_work']}\n - <b>от"
                           f" {price_amplifier[6]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[7]['type_work']}\n - <b>от"
                           f" {price_amplifier[7]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[8]['type_work']}\n - <b>от"
                           f" {price_amplifier[8]['price']} Руб. </b>\n\n"
                           f"💵{price_amplifier[9]['type_work']}\n - <b>от"
                           f" {price_amplifier[9]['price']} Руб. </b>\n\n",
                           parse_mode="HTML",
                           reply_markup=kb_price_repair_din_markup)


@dp.callback_query_handler(text='callback_example_works')
async def callback_example_works(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    with open(f'static/img/img_example_works/{(await get_users_lost_photo(callback.from_user.id))}.jpeg', 'rb') \
            as photo:
        await bot.send_photo(chat_id=callback.from_user.id, photo=photo, reply_markup=kb_photo_example_works)


@dp.callback_query_handler(text='callback_photo_back')
async def callback_photo_back(callback: types.callback_query):
    if (await get_users_lost_photo(callback.from_user.id)) > 1:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        (await update_lost_photo_users_down(callback.from_user.id))
        with open(f'static/img/img_example_works/{(await get_users_lost_photo(callback.from_user.id))}.jpeg', 'rb') \
                as photo:
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo, reply_markup=kb_photo_example_works)


@dp.callback_query_handler(text='callback_photo_forward')
async def callback_photo_back(callback: types.callback_query):
    if (await get_users_lost_photo(callback.from_user.id)) <= 32:
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        (await update_lost_photo_users_up(callback.from_user.id))
        with open(f'static/img/img_example_works/{(await get_users_lost_photo(callback.from_user.id))}.jpeg', 'rb') \
                as photo:
            await bot.send_photo(chat_id=callback.from_user.id, photo=photo, reply_markup=kb_photo_example_works)


# запись на установку автозвука //////////////////////////////////////////////////////////////////////////////////////
@dp.callback_query_handler(text='callback_sign_up_btn')
async def callback_sign_up_btn(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Выберете куда вы хотите записаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up)


@dp.callback_query_handler(text='callback_installation')
async def callback_installation(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите как к вам обращаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back)
    await Mydialog.state_sign_up_name.set()


# 1
@dp.message_handler(state=Mydialog.state_sign_up_name)
async def callback_installation_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        (await update_name_users(user_message, message.from_user.id))
        await Mydialog.state_sign_up_name.set()
        await bot.send_message(message.from_user.id, f"<b>Вас зовут</b> "
                                                     f"{user_message}?", parse_mode='HTML',
                               reply_markup=kb_sign_up_name)


# 2
@dp.callback_query_handler(text='callback_installation_no', state=Mydialog.state_sign_up_name)
async def callback_installation_no(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите как к вам обращаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back)
    await Mydialog.state_sign_up_name.set()


@dp.callback_query_handler(text='callback_sign_up_back', state=Mydialog.state_sign_up_name)
async def callback_sign_up_back(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Выберете куда вы хотите записаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up)


@dp.callback_query_handler(text='callback_installation_yes', state=Mydialog.state_sign_up_name)
async def callback_installation_yes(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите ваш номер телефона в формате'
                                                  ' 79XXXXXXXXX</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back_num)
    await Mydialog.state_sign_up_mobile_number.set()


@dp.message_handler(state=Mydialog.state_sign_up_mobile_number)
async def callback_installation_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        (await update_number_phone_users(user_message, message.from_user.id))
        await Mydialog.state_sign_up_mobile_number.set()
        await bot.send_message(message.from_user.id, f"<b>Это ваш номер телефона</b> "
                                                     f"{user_message}?", parse_mode='HTML', reply_markup=kb_sign_up_num)


@dp.callback_query_handler(text='callback_sign_up_installation_num_yes', state=Mydialog.state_sign_up_mobile_number)
async def callback_installation_yes(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    btn_resend_users = InlineKeyboardButton(text='Перезвонить',
                                            url=f'http://onmap.uz/tel/'
                                                f'{(await get_users_number_phone(callback.from_user.id))}')
    kb_admin_install = InlineKeyboardMarkup()
    kb_admin_install.add(btn_resend_users)
    await bot.send_message((await get_admin_users_with_role('installation')),
                           f'<b>{(await get_users_name(callback.from_user.id))}'
                           f' записался(лась) на установку акустики.\n\n'
                           f'перезвоните ему(ей) по номеру</b> {(await get_users_number_phone(callback.from_user.id))}',
                           reply_markup=kb_admin_install, parse_mode='HTML')
    await bot.send_message(callback.from_user.id, f'<b>Вы записались на установку акустики.'
                                                  f' В ближайшее время вам перезвонят по указаному вами номеру </b>'
                                                  f'{(await get_users_number_phone(callback.from_user.id))}'
                                                  f' <b>для уточнения времени</b>'
                           , parse_mode='HTML',
                           reply_markup=kb_sign_up_back_to_servis)


@dp.callback_query_handler(text='callback_sign_up_installation_num_no', state=Mydialog.state_sign_up_mobile_number)
async def callback_installation_yes(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите ваш номер телефона в формате'
                                                  ' 79XXXXXXXXX</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back_num)
    await Mydialog.state_sign_up_mobile_number.set()


@dp.callback_query_handler(text='callback_sign_up_back_num', state=Mydialog.state_sign_up_mobile_number)
async def callback_sign_up_back_(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Выберете куда вы хотите записаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
@dp.callback_query_handler(text='callback_car_service')
async def callback_car(callback: types.callback_query):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите как к вам обращаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back)
    await Mydialog.state_sign_up_name_car_service.set()


@dp.callback_query_handler(text='callback_sign_up_back', state=Mydialog.state_sign_up_name_car_service)
async def callback_sign_up_back(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Выберете куда вы хотите записаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up)


@dp.message_handler(state=Mydialog.state_sign_up_name_car_service)
async def callback_car_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        (await update_name_users(user_message, message.from_user.id))
        await Mydialog.state_sign_up_name_car_service.set()
        await bot.send_message(message.from_user.id, f"<b>Вас зовут</b> "
                                                     f"{user_message}?", parse_mode='HTML',
                               reply_markup=kb_sign_up_name_car_service)


@dp.callback_query_handler(text='callback_car_service_no', state=Mydialog.state_sign_up_name_car_service)
async def callback_car_no(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите как к вам обращаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back)
    await Mydialog.state_sign_up_name_car_service.set()


# ok

@dp.callback_query_handler(text='callback_car_service_yes', state=Mydialog.state_sign_up_name_car_service)
async def callback_car_yes(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите ваш номер телефона в формате'
                                                  ' 79XXXXXXXXX</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back_num)
    await Mydialog.state_sign_up_mobile_number_car_service.set()


@dp.message_handler(state=Mydialog.state_sign_up_mobile_number_car_service)
async def callback_car_state(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']
        (await update_number_phone_users(user_message, message.from_user.id))
        await Mydialog.state_sign_up_mobile_number_car_service.set()
        await bot.send_message(message.from_user.id, f"<b>Это ваш номер телефона</b> "
                                                     f"{user_message}?", parse_mode='HTML', reply_markup=kb_sign_up_num)


@dp.callback_query_handler(text='callback_sign_up_installation_num_yes',
                           state=Mydialog.state_sign_up_mobile_number_car_service)
async def callback_installation_yes(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    btn_resend_users = InlineKeyboardButton(text='Перезвонить',
                                            url=f'http://onmap.uz/tel/'
                                                f'{(await get_users_number_phone(callback.from_user.id))}')
    kb_admin_install = InlineKeyboardMarkup()
    kb_admin_install.add(btn_resend_users)
    await bot.send_message((await get_admin_users_with_role('car_service')),
                           f'<b>{(await get_users_name(callback.from_user.id))} записался(лась) в автосервис.\n\n'
                           f'перезвоните ему(ей) по номеру</b> {(await get_users_number_phone(callback.from_user.id))}',
                           reply_markup=kb_admin_install, parse_mode='HTML')
    await bot.send_message(callback.from_user.id, f'<b>Вы записались в автосервис.'
                                                  f' В ближайшее время вам перезвонят по указаному вами номеру </b>'
                                                  f'{(await get_users_number_phone(callback.from_user.id))}'
                                                  f' <b>для уточнения времени</b>'
                           , parse_mode='HTML',
                           reply_markup=kb_sign_up_back_to_servis)


@dp.callback_query_handler(text='callback_sign_up_installation_num_no',
                           state=Mydialog.state_sign_up_mobile_number_car_service)
async def callback_installation_yes(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Укажите ваш номер телефона в формате'
                                                  ' 79XXXXXXXXX</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up_only_back_num)
    await Mydialog.state_sign_up_mobile_number_car_service.set()


@dp.callback_query_handler(text='callback_sign_up_back_num', state=Mydialog.state_sign_up_mobile_number_car_service)
async def callback_sign_up_back_(callback: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_message(callback.from_user.id, '<b>Выберете куда вы хотите записаться</b>', parse_mode='HTML',
                           reply_markup=kb_sign_up)


if __name__ == '__main__':
    executor.start_polling(dp)
