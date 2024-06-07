from WB.prices.schemas import TaskAlreadyExistsErrorData
from dataclasses import dataclass


@dataclass
class TaskAlreadyExistsError:

    Data: TaskAlreadyExistsErrorData
    #  Флаг ошибки
    error: bool
    #  Текст ошибки
    errorText: str
