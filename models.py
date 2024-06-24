from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Model(DeclarativeBase):
    pass

#Для создания моделей всегда нужен класс от которого наследуемся
#Модель соотвествует одной таблице в бд
#Orm-Объекто-реляционное отображение, то есть связывает бд с кодом ООП(крч таблицы это теперь классы)
class TaskOrm(Model):
    __tablename__="tasks"
    id: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str|None]