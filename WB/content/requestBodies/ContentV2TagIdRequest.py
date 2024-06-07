from dataclasses import dataclass


@dataclass
class ContentV2TagIdRequest:
    """
    Изменение тега
    Метод позволяет изменять информацию о теге (имя и цвет).
    """
    #  Цвет тега
    color: str
    #  Имя тега
    name: str
