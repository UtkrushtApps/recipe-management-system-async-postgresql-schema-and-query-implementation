import asyncpg
import asyncio

DB_CONFIG = {
    'user': 'recipe_user',
    'password': 'recipe_pass',
    'database': 'recipe_db',
    'host': 'db',
    'port': 5432
}

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(**DB_CONFIG)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def fetchrow(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def execute(self, query, *args):
        async with self.pool.acquire() as conn:
            return await conn.execute(query, *args)

db = Database()

async def get_db():
    if not db.pool:
        await db.connect()
    return db
