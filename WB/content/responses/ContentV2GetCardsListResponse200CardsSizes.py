from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200CardsSizes:
    #  Числовой идентификатор размера для данного артикула WB
    chrtID: int
    #  Размер товара (А, XXL, 57 и др.)
    techSize: str
    #  Российский размер товара
    wbSize: str
    #  Баркод товара
    skus: List[str]
