from WB.content.responses import ContentV2CardsLimitsResponse200Data
from dataclasses import dataclass


@dataclass
class ContentV2CardsLimitsResponse200:
    """
    Лимиты по КТ

    Метод позволяет получить отдельно бесплатные и платные лимиты продавца на создание карточек товаров. <br> Формула для получения количества карточек, которые можно создать: (`freeLimits` + `paidLimits`) - Количество созданных карточек.<br> Созданными считаются все карточки, которые можно получить методами "Список НМ" и "Список НМ, находящихся в корзине".
    
    """

    Data: ContentV2CardsLimitsResponse200Data
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
