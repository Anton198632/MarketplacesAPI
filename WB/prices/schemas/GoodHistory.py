from WB.prices.schemas import GoodStatus
from dataclasses import dataclass


@dataclass
class GoodHistory:
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

    status: GoodStatus
    #  Текст ошибки
    #  
    #  <blockquote class="spoiler">
    #    <p class="descr">Ошибка <co
    #  de>The product is in quarantine</code> возникает, если новая цена со ски
    #  дкой хотя бы в 3 раза меньше старой. Вы можете изменить цену или скидку 
    #  с помощью API либо вывести товар из карантина <a href="https://seller.wi
    #  ldberries.ru/discount-and-prices/quarantine">в личном кабинете</a></p>
    #  <
    #  /blockquote>
    errorText: str
