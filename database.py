from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from models import Model

#Создается асинхронное подключение отвечающие за отправку запросов в бд engine
engine=create_async_engine("sqlite+aiosqlite:///tasks.db")
#Создаем фабрику сессий для работы с моделями данных а не со словарями
new_session=async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:#with гарантирует закрытие подключения к бд
        await conn.run_sync(Model.metadata.drop_all)