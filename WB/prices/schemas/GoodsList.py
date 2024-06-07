from WB.prices.schemas import GoodsListSizes
from dataclasses import dataclass
from typing import List


@dataclass
class GoodsList:
    #  Артикул Wildberries
    nmID: int
    #  Артикул продавца
    vendorCode: str
    #  Размер
    Sizes: List[GoodsListSizes]
    #  Валюта, по стандарту ISO 4217
    currencyIsoCode4217: str
    #  Скидка, %
    discount: int
    #  Можно ли устанавливать цены отдельно для разных размеров: `true` — можно
    #  , `false` — нельзя. Эта возможность зависит от категории товара
    editableSizePrice: bool
