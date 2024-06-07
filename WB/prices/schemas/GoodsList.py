from WB.prices.schemas import GoodsListSizes
from typing import List
from dataclasses import dataclass


@dataclass
class GoodsList:
    #  Артикул Wildberries
    nmID: int
    #  Артикул продавца
    vendorCode: str
    #  Размер
    sizes: List[GoodsListSizes]
    #  Валюта, по стандарту ISO 4217
    currencyIsoCode4217: str
    #  Скидка, %
    discount: int
    #  Можно ли устанавливать цены отдельно для разных размеров: `true` — можно
    #  , `false` — нельзя. Эта возможность зависит от категории товара
    editableSizePrice: bool
