from dataclasses import dataclass


@dataclass
class SizeGood:
    #  Артикул Wildberries
    nmID: int
    #  ID размера. Можно получить с помощью метода [Получение списка товаров по
    #   артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/g
    #  et), поле `sizeID`. В методах контента это поле `chrtID`
    sizeID: int
    #  Артикул продавца
    vendorCode: str
    #  Цена
    price: int
    #  Валюта, по стандарту ISO 4217
    currencyIsoCode4217: str
    #  Цена со скидкой
    discountedPrice: int
    #  Скидка, %
    discount: int
    #  Размер товара
    techSizeName: str
    #  Можно ли устанавливать цены отдельно для разных размеров: `true` — можно
    #  , `false` — нельзя. Эта возможность зависит от категории товара
    editableSizePrice: bool
