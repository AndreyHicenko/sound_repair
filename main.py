from aiogram import Bot, Dispatcher, types
import asyncio
import psycopg2
from config import TOKEN
from aiogram.utils import executor
import logging
from keyboards.keyboard_start import *
from keyboards.keyboard_servises import *
from keyboards.keyboard_kontakt import *
from keyboards.keyboard_price_lists import *
from datebase.query_datebase import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("<b>Здравствуйте!</b> Вас приветствует<b>"
                         " бот студии автозвука SOUND REPAIR.</b>",
                         parse_mode="HTML", reply_markup=kb_start)


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


if __name__ == '__main__':
    executor.start_polling(dp)
