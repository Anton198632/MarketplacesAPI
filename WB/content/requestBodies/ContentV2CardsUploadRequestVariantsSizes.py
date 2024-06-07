from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUploadRequestVariantsSizes:
    #  Размер товара (XL, 45 и др.)
    techSize: str
    #  Российский размер товара
    wbSize: str
    #  Цена товара
    price: int
    #  Баркод. Если не указать, сгенерируется системой автоматически.
    skus: List[str]
