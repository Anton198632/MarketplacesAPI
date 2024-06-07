from dataclasses import dataclass


@dataclass
class Good:
    #  Артикул Wildberries
    nmID: int
    #  Цена. Валюту можно получить с помощью метода [Получение списка товаров п
    #  о артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/
    #  get), поле `currencyIsoCode4217`
    price: int
    #  Скидка, %
    discount: int
