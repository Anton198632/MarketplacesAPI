from WB.prices.schemas import SupplierTaskMetadata
from dataclasses import dataclass


@dataclass
class ResponseTaskHistory:
    """
    Состояние загрузки

    
    """

    data: SupplierTaskMetadata
    #  Флаг ошибки
    error: bool
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
