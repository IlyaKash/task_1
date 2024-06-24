from database import new_session
from models import TaskOrm
from sqlalchemy import select
from schemas import STaskAdd, STask


#Это относится к 3 пункту в progres.txt
# async def add_task(data: dict) -> int:
#     '''
#         Функция использует фабрику сессий new_session и модель TaskOrm чтоб добавить в таблицу tasks новую строку.
#         async with(асинхр.контекстный менеджер) позволяет автоматически закрывать сессию при выходе из менеджера, чтоб не приходилось каждый раз закрывать сессию session.close()
#     '''
#     async with new_session() as session:#Используем фабрику сессий
#         new_task=TaskOrm(**data)#Создает новюу строку таблицы но хранит ее внутри FastAPI приложения(бд еще ничего о ней не знает)
#         session.add(new_task)#Добавляет новую строку в объект сессии, чтоб SQLAlchemy Знала какие изменения нужно добавить в бд(но бд до сих пор ничего не знает)
#         await session.flush()#Отправляет в бд запрос вида INSERT INTO tasks (name, description) VALUES ('Jack', NULL) RETURNING id, но еще не завершает транзакцию(то есть изменения все еще не в бд)
#         #Функция flush() позволяет получить значение id новой задачи которое мы return в конце функции
#         await session.commit()#После этого изменнеия находятся в бд(завершение транзакции)
#         return new_task.id
#         #Заметьте, что любой код, который не выполняется асинхронно, не взаимодействует с базой данных, 
#         #а все асинхронные операции отправляют запросы в базу. Помните об этом, когда будете работать с объектом сессии.


# async def get_task():
#     '''Делаем простой select всех строк бд'''
#     #Учитывая, что мы просим выбрать все объекты класса TaskOrm,
#     #SQLAlchemy конвертирует ответ от базы данных к экземплярам модели TaskOrm
#     async with new_session() as session:
#         query=select(TaskOrm)
#         result= await session.execute(query)#result - это итератор, по которому нужно пройтись и выбрать все нужные результаты
#         task_model=result.scalars().all()#для этого мы вводим эту команду
#         return task_model


#Относится к пункту 4

#Так как обе функции обращаются к одной таблице лучше будет объеденить их в один класс
#Такие классы, которые взаимодействуют с определенной таблицей и отвечают за функции добавления, 
#изменения, выборки и удаления строк, называют репозиториями, так как они используют соответствующий паттерн. 

class TaskRepository:
    @classmethod
    async def add_task(cls, task: STaskAdd)->int:
        #Теперь ты получаем не случайный словарь а пайдентик схему
        async with new_session() as session:
            data=task.model_dump()#Преобразуем ее в словарь 
            new_task=TaskOrm(**data)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id
    
    @classmethod
    async def get_tasks(cls)->list[STask]:
        async with new_session() as session:
            query=select(TaskOrm)
            result=await session.execute(query)
            task_models=result.scalars().all()
            #При отдаче мы предварительно конвертируем их в пайдентик схему STask
            tasks=[STask.model_validate(task_model) for task_model in task_models]
            return tasks

