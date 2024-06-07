from WB.prices.schemas import TaskCreatedData
from dataclasses import dataclass


@dataclass
class TaskCreated:

    data: TaskCreatedData
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
