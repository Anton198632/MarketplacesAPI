from WB.content.responses import ContentV2DirectoryTnvedResponse200Data
from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2DirectoryTnvedResponse200:
    """
    ТНВЭД код

    С помощью данного метода можно получить список ТНВЭД кодов по ID предмета и фильтру по ТНВЭД коду. <span class="newM">new</span>
    """
    #  Данные
    Data: List[ContentV2DirectoryTnvedResponse200Data]
    #  Флаг наличия ошибки
    error: bool
    #  Текст ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
