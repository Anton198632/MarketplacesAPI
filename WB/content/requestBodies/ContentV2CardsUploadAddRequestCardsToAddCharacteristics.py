from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadAddRequestCardsToAddCharacteristics:
    #  ID характеристики
    id: int
    #  Значение характеристики. Тип значения зависит от типа характеристики
    value: NoneType
