from WB.content.responses import ContentV2CardsErrorListResponse200Data
from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsErrorListResponse200:
    """
    Список несозданных номенклатур (НМ) с ошибками

    Метод позволяет получить список НМ и список ошибок которые произошли во время создания КТ. <br>`ВАЖНО`: Для того чтобы убрать НМ из ошибочных, надо повторно сделать запрос с исправленными ошибками на создание КТ.
    
    """

    Data: List[ContentV2CardsErrorListResponse200Data]
    #  Флаг ошибки.
    error: bool
    #  Описание ошибки.
    errorText: str
    #  Дополнительные ошибки.
    additionalErrors: str
