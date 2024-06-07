from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200CardsCharacteristics:
    #  Идентификатор характеристики
    id: int
    #  Название характеристики
    name: str
    #  Значение характеристики. Тип значения зависит от типа характеристики
    value: NoneType
