from pydantic import BaseModel, ConfigDict

#Схема для добавления новой задачи
class STaskAdd(BaseModel):
    name: str
    description: str|None = None


#Схема для чтения задач из баз данных
class STask(STaskAdd):
    id: int #id - первичный ключ в таблице
    model_config=ConfigDict(from_attributes=True)

#Схема из пункта 5 про роутер
class STaskId(BaseModel):
    id: int
