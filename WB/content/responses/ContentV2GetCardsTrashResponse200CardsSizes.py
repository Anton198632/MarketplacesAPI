from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2GetCardsTrashResponse200CardsSizes:
    #  ID размера
    chrtID: int
    #  Размер товара
    techSize: str
    #  Российский размер товара
    wbSize: str
    #  Массив баркодов
    skus: List[str]
