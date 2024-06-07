from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2DirectoryKindsResponse200:
    """
    Пол

    Получение значения характеристики пол.
    """
    #  Массив значений для хар-ки Пол
    data: List[str]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
