from WB.content.requests.trash.cards_trash_data import CardsDeleteTrashData
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.trash.response_trash import ResponseTrash
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/cards/delete/trash"


class RequestCardsDeleteTrashAPI(AbsRequestExecutor):
    """
    **Перенос НМ в корзину**

    Метод позволяет перенести НМ в корзину.
     Перенос карточки в корзину не является удалением карточки.
     ВАЖНО: При переносе НМ в корзину, данная НМ выходит из КТ, то есть ей
      присваивается новый imtID.

    Карточка товара удаляется автоматически, если лежит в корзине больше
     30 дней.
    Корзина зачищается от карточек, лежащих в ней более 30 дней, каждую ночь
     по Московскому времени.
    """

    def execute(
        self, cards_delete_trash_data: CardsDeleteTrashData
    ) -> ResponseTrash:
        response = self._post(url=URL, json=to_dict(cards_delete_trash_data))
        if response:
            return from_dict(ResponseTrash, response)
