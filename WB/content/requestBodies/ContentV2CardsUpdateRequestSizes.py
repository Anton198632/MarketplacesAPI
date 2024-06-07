from dataclasses import dataclass
from typing import List


@dataclass
class ContentV2CardsUpdateRequestSizes:
    #  Числовой идентификатор размера для данного артикула Wildberries
    #  Обязател
    #  ен к заполнению для существующих размеров.
    #  Для добавляемых размеров не у
    #  казывается.
    chrtID: int
    #  Размер товара (XL, S, 45 и др.)
    techSize: str
    #  Российский размер товара
    wbSize: str
    #  Баркод
    skus: List[str]
