from dataclasses import dataclass


@dataclass
class TaskAlreadyExistsErrorData:
    #  ID загрузки
    id: int
    #  Флаг дублирования загрузки: `true` — такая загрузка уже есть
    alreadyExists: bool
