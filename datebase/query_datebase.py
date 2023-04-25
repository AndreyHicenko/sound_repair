import asyncpg
from config import *
import asyncio


async def search_db_price_din():
    conn = await asyncpg.connect(
        DATABASE)
    row = conn.fetch('SELECT * FROM table_price_dinamic')
    return await row


async def search_db_price_sub():
    conn = await asyncpg.connect(
        DATABASE)
    row = conn.fetch('SELECT * FROM table_price_subwoofer')
    return await row


async def search_db_price_amplifier():
    conn = await asyncpg.connect(
        DATABASE)
    row = conn.fetch('SELECT * FROM table_price_amplifier')
    return await row


async def search_admin_users():
    conn = await asyncpg.connect(
        DATABASE)
    row = conn.fetch('SELECT * FROM table_admin_id')
    return await row


async def search_users_id():
    conn = await asyncpg.connect(
        DATABASE)
    row = conn.fetch('SELECT * FROM table_users_id')
    return await row


async def add_users_id(values):
    conn = await asyncpg.connect(
        DATABASE)
    statement = """INSERT INTO table_users_id (id_users) VALUES($1);"""
    await conn.execute(statement, values)


async def update_lost_message_admin(message, id):
    conn = await asyncpg.connect(
        DATABASE)
    statement = """UPDATE table_admin_id SET admin_lost_message = $1 WHERE id_admin_users = $2"""
    await conn.execute(statement, message, id)


async def get_admin_lost_message(id_admin_users):
    conn = await asyncpg.connect(
        DATABASE)
    query = """SELECT admin_lost_message FROM table_admin_id WHERE id_admin_users = $1"""
    return await conn.fetchval(query, id_admin_users)


async def get_users_lost_photo(id_users):
    conn = await asyncpg.connect(
        DATABASE)
    query = """SELECT lost_photo FROM table_users_id WHERE id_users = $1"""
    return await conn.fetchval(query, id_users)


async def update_lost_photo_users_up(id):
    lost_photo = (await get_users_lost_photo(id)) + 1
    conn = await asyncpg.connect(
        DATABASE)
    statement = """UPDATE table_users_id SET lost_photo = $1 WHERE id_users = $2"""
    await conn.execute(statement, lost_photo, id)


async def update_lost_photo_users_down(id):
    lost_photo = (await get_users_lost_photo(id)) - 1
    conn = await asyncpg.connect(
        DATABASE)
    statement = """UPDATE table_users_id SET lost_photo = $1 WHERE id_users = $2"""
    await conn.execute(statement, lost_photo, id)


async def update_name_users(name, id):
    conn = await asyncpg.connect(
        DATABASE)
    statement = """UPDATE table_users_id SET name = $1 WHERE id_users = $2"""
    await conn.execute(statement, name, id)


async def update_number_phone_users(number_phone, id):
    conn = await asyncpg.connect(
        DATABASE)
    statement = """UPDATE table_users_id SET number_phone = $1 WHERE id_users = $2"""
    await conn.execute(statement, number_phone, id)


async def get_users_name(id_users):
    conn = await asyncpg.connect(
        DATABASE)
    query = """SELECT name FROM table_users_id WHERE id_users = $1"""
    return await conn.fetchval(query, id_users)


async def get_users_number_phone(id_users):
    conn = await asyncpg.connect(
        DATABASE)
    query = """SELECT number_phone FROM table_users_id WHERE id_users = $1"""
    return await conn.fetchval(query, id_users)


async def get_admin_users_with_role(role):
    conn = await asyncpg.connect(
        DATABASE)
    query = """SELECT id_admin_users FROM table_admin_id WHERE role_admin = $1"""
    return await conn.fetchval(query, role)
