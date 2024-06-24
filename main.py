from fastapi import FastAPI, Depends
from schemas import STaskAdd
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
#импортируем роутер с 2 эндпоинтами(пункт 5)
from router import router as tasks_router

#Жизненный цикл приложения
@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")

app=FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

@app.get("/")
async def home():
    return {"data": "hello wordl"}

@app.post("/")
async def add_task(task:STaskAdd=Depends()):
    return {"data": task}