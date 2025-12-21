from fastapi import FastAPI
from app.tasks import create_task, get_tasks
from app.database import init_db
import asyncio
from app.workers import worker_loop

app = FastAPI(title="Async Task Platform")

@app.on_event("startup")
async def startup():
    await init_db()
    asyncio.create_task(worker_loop())

@app.post("/tasks")
async def add_task(name: str):
    return await create_task(name)

@app.get("/tasks")
async def list_tasks():
    return await get_tasks()