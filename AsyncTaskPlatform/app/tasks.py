from app.database import DATABASE
import aiosqlite

async def create_task(name: str):
    async with aiosqlite.connect(DATABASE) as db:
        await db.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", (name, "pending"))
        await db.commit()
    return {"status": "created"}

async def get_tasks():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute("SELECT id, name, status FROM tasks")
        rows = await cursor.fetchall()
        return [{"id": r[0], "name": r[1], "status": r[2]} for r in rows]