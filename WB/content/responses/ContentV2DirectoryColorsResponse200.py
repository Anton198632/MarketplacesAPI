from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2DirectoryColorsResponse200:
    """
    Цвет
    Получение значения характеристики цвет.
    """

    data: NoneType
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
