from WB.prices.schemas import TaskAlreadyExistsErrorData
from dataclasses import dataclass


@dataclass
class TaskAlreadyExistsError:

    data: TaskAlreadyExistsErrorData
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
