from typing import List
from WB.content.responses import ContentV2ObjectAllResponse200Data
from dataclasses import dataclass


@dataclass
class ContentV2ObjectAllResponse200:
    """
    Список предметов (подкатегорий)
    С помощью данного метода можно получить список всех доступных предметов, ро
    дительских категорий предметов, и их идентификаторов.  <span class="newM">n
    ew</span>
    """
    #  Подкатегории (предметы)
    data: List[ContentV2ObjectAllResponse200Data]
    #  Флаг наличия ошибки
    error: bool
    #  Текст ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
