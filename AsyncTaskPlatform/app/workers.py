import asyncio
from app.tasks import get_tasks

async def worker_loop():
    while True:
        tasks = await get_tasks()
        for task in tasks:
            if task["status"] == "pending":
                print(f"Processing task: {task['name']}")
                # Симуляція роботи
                await asyncio.sleep(1)
                # Тут можна оновити статус у базі
        await asyncio.sleep(5)