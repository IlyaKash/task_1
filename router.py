from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId

router=APIRouter(
    prefix="/tasks",#каждый эндпоинт будет иметь префикс /tasks
    tags=["Таски"],
)

#Ниже 2 эндпоинта
@router.post("")
async def add_task(task:STaskAdd=Depends())->STaskId:
    new_task_id=await TaskRepository.add_task(task)
    return {"id": new_task_id}

@router.get("")
async def get_tasks()-> list[STask]:
    tasks=await TaskRepository.get_tasks()
    return tasks

# В файле router.py мы используем созданный ранее репозиторий, 
# аннотации типов и возвращаемый тип функций. 
# Это позволяет нам добавить валидацию возвращаемых клиенту данных и улучшить документацию к API: