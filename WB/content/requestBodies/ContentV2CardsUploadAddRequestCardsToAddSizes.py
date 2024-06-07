from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2CardsUploadAddRequestCardsToAddSizes:
    #  Размер товара (XL, 42 и др.)
    techSize: str
    #  Российский размер товара
    wbSize: str
    #  Цена товара
    price: int
    #  Баркод
    skus: List[str]
