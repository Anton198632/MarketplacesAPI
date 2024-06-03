from WB.content.requests.trash.cards_trash_data import CardsRecoveryData
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.trash.response_trash import ResponseTrash
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/cards/recover"


class RequestCardsRecoverAPI(AbsRequestExecutor):
    """
    **Восстановление НМ из корзины**

    Метод позволяет восстановить НМ из корзины.
    ВАЖНО: При восстановлении НМ из корзины она не возвращается в КТ в
     которой была до переноса в корзину, то есть imtID остается тот же,
      что и был у НМ в корзине.
    """

    def execute(
        self, cards_recovery_data: CardsRecoveryData
    ) -> ResponseTrash:
        response = self._post(url=URL, json=to_dict(cards_recovery_data))
        if response:
            return from_dict(ResponseTrash, response)
