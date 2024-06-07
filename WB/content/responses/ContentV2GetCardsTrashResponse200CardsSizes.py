from typing import List
from dataclasses import dataclass


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
