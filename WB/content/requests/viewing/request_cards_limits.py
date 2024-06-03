from WB.request_executor import AbsRequestExecutor, SERVER

from WB.content.responses.viewing.response_cards_limits import ResponseCardsLimits
from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/cards/limits"


class RequestCardsLimitsAPI(AbsRequestExecutor):
    """
    **Лимиты по КТ**

    Метод позволяет получить отдельно бесплатные и платные лимиты продавца на
     создание карточек товаров. <br> Формула для получения количества карточек,
      которые можно создать: (`freeLimits` + `paidLimits`) - Количество
       созданных карточек.<br> Созданными считаются все карточки, которые
        можно получить методами "Список НМ" и "Список НМ, находящихся в
         корзине".

    """

    def execute(self) -> ResponseCardsLimits:
        response = self._get(URL)
        if response:
            return from_dict(ResponseCardsLimits, response)
