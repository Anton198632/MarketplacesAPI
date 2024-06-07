from WB.content.responses import ContentV2ObjectAllResponse200Data
from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2ObjectAllResponse200:
    """
    Список предметов (подкатегорий)

    С помощью данного метода можно получить список всех доступных предметов, родительских категорий предметов, и их идентификаторов.  <span class="newM">new</span>
    """
    #  Подкатегории (предметы)
    Data: List[ContentV2ObjectAllResponse200Data]
    #  Флаг наличия ошибки
    error: bool
    #  Текст ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
