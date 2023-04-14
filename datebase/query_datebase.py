import asyncpg
import asyncio
from config import *


async def search_db_price_din():
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    row = conn.fetch('SELECT * FROM table_price_dinamic')
    return await row


async def search_db_price_sub():
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    row = conn.fetch('SELECT * FROM table_price_subwoofer')
    return await row


async def search_db_price_amplifier():
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    row = conn.fetch('SELECT * FROM table_price_amplifier')
    return await row


async def search_admin_users():
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    row = conn.fetch('SELECT * FROM table_admin_id')
    return await row


async def search_users_id():
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    row = conn.fetch('SELECT * FROM table_users_id')
    return await row


async def add_users_id(values):
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    statement = """INSERT INTO table_users_id (id_users) VALUES($1);"""
    await conn.execute(statement, values)


async def update_lost_message_admin(message, id):
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    statement = """UPDATE table_admin_id SET admin_lost_message = $1 WHERE id_admin_users = $2"""
    await conn.execute(statement, message, id)


async def get_admin_lost_message(id_admin_users):
    conn = await asyncpg.connect(host=HOST_DB,
                                 port=PORT_DB,
                                 user=USER_DB,
                                 password=PASSWORD_DB,
                                 database=DATABASE_NAME_DB)
    query = """SELECT admin_lost_message FROM table_admin_id WHERE id_admin_users = $1"""
    return await conn.fetchval(query, id_admin_users)
