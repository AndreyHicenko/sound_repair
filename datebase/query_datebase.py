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
