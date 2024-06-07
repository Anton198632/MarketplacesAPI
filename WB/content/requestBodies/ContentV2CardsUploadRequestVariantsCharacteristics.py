from dataclasses import dataclass
from types import NoneType


@dataclass
class ContentV2CardsUploadRequestVariantsCharacteristics:
    #  Идентификатор характеристики
    id: int
    #  Значение характеристики. Тип значения зависит от типа характеристики
    value: NoneType
