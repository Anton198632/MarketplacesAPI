from WB.content.responses import (
    ContentV2GetCardsTrashResponse200CardsCharacteristics,
)
from WB.content.responses import (
    ContentV2GetCardsTrashResponse200CardsDimensions,
)
from WB.content.responses import ContentV2GetCardsTrashResponse200CardsPhotos
from WB.content.responses import ContentV2GetCardsTrashResponse200CardsSizes
from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsTrashResponse200Cards:
    #  Артикул WB
    nmID: int
    #  Артикул продавца
    vendorCode: str
    #  Идентификатор предмета
    subjectID: str
    #  Название предмета
    subjectName: str
    #  Массив фото
    Photos: List[ContentV2GetCardsTrashResponse200CardsPhotos]
    #  URL видео
    video: str
    #  Массив размеров
    Sizes: List[ContentV2GetCardsTrashResponse200CardsSizes]

    Dimensions: ContentV2GetCardsTrashResponse200CardsDimensions
    #  Массив характеристик, при наличии
    Characteristics: List[ContentV2GetCardsTrashResponse200CardsCharacteristics]

    createdAt: str

    trashedAt: str
