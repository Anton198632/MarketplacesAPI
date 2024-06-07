from dataclasses import dataclass


@dataclass
class TaskCreatedData:
    #  ID загрузки
    id: int
    #  Флаг дублирования загрузки: `true` — такая загрузка уже есть
    alreadyExists: bool
