from WB.content.responses import ContentV2GetCardsListResponse200CardsSizes
from WB.content.responses import ContentV2GetCardsListResponse200CardsPhotos
from WB.content.responses import (
    ContentV2GetCardsListResponse200CardsDimensions,
)
from typing import List
from WB.content.responses import ContentV2GetCardsListResponse200CardsTags
from WB.content.responses import (
    ContentV2GetCardsListResponse200CardsCharacteristics,
)
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200Cards:
    #  Артикул WB
    nmID: int
    #  Идентификатор КТ.  Артикулы WB из одной КТ будут иметь одинаковый imtID
    imtID: int
    #  Внутренний технический идентификатор товара
    nmUUID: str
    #  Идентификатор предмета
    subjectID: int
    #  Артикул продавца
    vendorCode: str
    #  Название предмета
    subjectName: str
    #  Бренд
    brand: str
    #  Наименование товара
    title: str
    #  Массив фото
    Photos: List[ContentV2GetCardsListResponse200CardsPhotos]
    #  URL видео
    video: str
    #  Габариты упаковки товара, см
    Dimensions: ContentV2GetCardsListResponse200CardsDimensions
    #  Характеристики
    Characteristics: List[ContentV2GetCardsListResponse200CardsCharacteristics]
    #  Размеры товара
    Sizes: List[ContentV2GetCardsListResponse200CardsSizes]
    #  Теги
    Tags: List[ContentV2GetCardsListResponse200CardsTags]
    #  Дата создания
    createdAt: str
    #  Дата изменения
    updatedAt: str
