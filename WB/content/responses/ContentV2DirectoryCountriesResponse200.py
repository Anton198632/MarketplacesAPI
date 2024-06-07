from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2DirectoryCountriesResponse200:
    """
    Страна Производства

    Получение значения характеристики Страна Производства.
    """

    data: NoneType
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
