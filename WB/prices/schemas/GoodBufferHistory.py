from WB.prices.schemas import GoodStatusBuffer
from dataclasses import dataclass


@dataclass
class GoodBufferHistory:
    #  Артикул Wildberries
    nmID: int
    #  Артикул продавца
    vendorCode: str
    #  ID размера. В методах контента это поле `chrtID`
    sizeID: int
    #  Размер
    techSizeName: str
    #  Цена
    price: int
    #  Валюта, по стандарту ISO 4217
    currencyIsoCode4217: str
    #  Скидка, %
    discount: int

    status: GoodStatusBuffer
    #  Текст ошибки
    errorText: str
