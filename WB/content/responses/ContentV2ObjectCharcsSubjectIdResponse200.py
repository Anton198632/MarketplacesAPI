from WB.content.responses import (
    ContentV2ObjectCharcs{subjectId}Response200Data,
)
from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2ObjectCharcsSubjectIdResponse200:
    """
    Характеристики предмета (подкатегории)

    Получение списка характеристик предмета по его ID. <span class="newM">new</span>
    """
    #  Данные
    Data: List[ContentV2ObjectCharcsSubjectIdResponse200Data]
    #  Флаг наличия ошибки
    error: bool
    #  Текст ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
