from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListRequestSettingsFilter:
    #  Фильтр по фото:
    #    
    #    * `0` — только карточки без фото
    #    * `1` — только к
    #  арточки с фото
    #    * `-1` — все карточки товара
    withPhoto: int
    #  Поиск по артикулу продавца, артикулу WB, баркоду
    textSearch: str
    #  Поиск по ID тегов
    tagIDs: List[int]
    #  Фильтр по категории. `true` - только разрешённые, `false` - все. Не испо
    #  льзуется в песочнице.
    allowedCategoriesOnly: bool
    #  Поиск по id предметов
    objectIDs: List[int]
    #  Поиск по брендам
    brands: List[str]
    #  Поиск по идентификатору КТ
    imtID: int
