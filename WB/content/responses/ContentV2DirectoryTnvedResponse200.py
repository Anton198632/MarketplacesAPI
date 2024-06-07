from WB.content.responses import ContentV2DirectoryTnvedResponse200Data
from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2DirectoryTnvedResponse200:
    """
    ТНВЭД код
    С помощью данного метода можно получить список ТНВЭД кодов по ID предмета и
     фильтру по ТНВЭД коду. <span class="newM">new</span>
    """
    #  Данные
    data: List[ContentV2DirectoryTnvedResponse200Data]
    #  Флаг наличия ошибки
    error: bool
    #  Текст ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
