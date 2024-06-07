from dataclasses import dataclass
from typing import List
from WB.content.responses import (
    ContentV2GetCardsTrashResponse200CardsDimensions,
)
from WB.content.responses import (
    ContentV2GetCardsTrashResponse200CardsCharacteristics,
)
from WB.content.responses import ContentV2GetCardsTrashResponse200CardsSizes
from WB.content.responses import ContentV2GetCardsTrashResponse200CardsPhotos


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
    photos: List[ContentV2GetCardsTrashResponse200CardsPhotos]
    #  URL видео
    video: str
    #  Массив размеров
    sizes: List[ContentV2GetCardsTrashResponse200CardsSizes]

    dimensions: ContentV2GetCardsTrashResponse200CardsDimensions
    #  Массив характеристик, при наличии
    characteristics: List[ContentV2GetCardsTrashResponse200CardsCharacteristics]

    createdAt: str

    trashedAt: str
