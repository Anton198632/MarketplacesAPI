from dataclasses import dataclass


@dataclass
class GoodsListSizes:
    #  ID размера. В методах контента это поле `chrtID`
    sizeID: int
    #  Цена
    price: int
    #  Цена со скидкой
    discountedPrice: int
    #  Размер товара
    techSizeName: str
