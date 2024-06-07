from WB.content.responses import ContentV2CardsErrorListResponse200Data
from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2CardsErrorListResponse200:
    """
    Список несозданных номенклатур (НМ) с ошибками
    Метод позволяет получить список НМ и список ошибок которые произошли во вре
    мя создания КТ. <br>`ВАЖНО`: Для того чтобы убрать НМ из ошибочных, надо по
    вторно сделать запрос с исправленными ошибками на создание КТ.
    """

    data: List[ContentV2CardsErrorListResponse200Data]
    #  Флаг ошибки.
    error: bool
    #  Описание ошибки.
    errorText: str
    #  Дополнительные ошибки.
    additionalErrors: str
