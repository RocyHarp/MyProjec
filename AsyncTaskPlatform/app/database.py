import aiosqlite

DATABASE = "tasks.db"

async def init_db():
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, status TEXT)"
        )
        await db.commit()