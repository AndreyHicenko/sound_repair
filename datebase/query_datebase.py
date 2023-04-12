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
