from typing import List

from WB.content.requests.loading.cards_update_data import Product
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.loading.response_card_create import (
    ResponseCardCreate,
)
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/cards/update"


class RequestCardsUpdateAPI(AbsRequestExecutor):
    """
    **Редактирование КТ**

    Обновляет карточку товара.
    Нельзя редактировать или удалить баркоды, но можно добавить баркод
     к существующему. Параметры `photos`, `video` и `tags` передавать не
      обязательно, их нельзя редактировать или удалять в этом методе.

    Если ответ Успешно (200), но какие-то карточки не изменились, проверьте
     ошибки с помощью метода `Список несозданных номенклатур (НМ) с
      ошибками`.

    В одном запросе можно отредактировать максимум 3000 номенклатур
    (`nmID`). Максимальный размер запроса 10 Мб.

    Габариты товаров можно указать только в **сантиметрах**.
    """

    def execute(self, products: List[Product]) -> ResponseCardCreate:
        response = self._post(url=URL, json=to_dict(products))
        if response:
            return from_dict(ResponseCardCreate, response)
