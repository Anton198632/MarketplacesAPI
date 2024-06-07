from dataclasses import dataclass


@dataclass
class SizeGoodReq:
    #  Артикул Wildberries
    nmID: int
    #  ID размера. Можно получить с помощью метода [Получение списка товаров по
    #   артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/g
    #  et), поле `sizeID`. В методах контента это поле `chrtID`
    sizeID: int
    #  Цена. Валюту можно получить с помощью метода [Получение списка товаров п
    #  о артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/
    #  get), поле `currencyIsoCode4217`
    price: int
