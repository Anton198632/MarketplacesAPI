from types import NoneType
from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadRequestVariantsCharacteristics:
    #  Идентификатор характеристики
    id: int
    #  Значение характеристики. Тип значения зависит от типа характеристики
    value: NoneType
