from WB.content.requests.loading.cards_upload_add_data import UploadAddData
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.loading.response_card_create import ResponseCardCreate
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/cards/upload/add"


class RequestCardsUploadAddAPI(AbsRequestExecutor):
    """
    **Добавление НМ к КТ'**

    Метод позволяет добавить к карточке товара новую номенклатуру.
     <span class="newM">new</span> <br>
    Добавление НМ к КТ происходит асинхронно, после отправки запрос становится
      в очередь на обработку.<br>
      `Важно!` Если после успешной отправки запроса номенклатура не создалась,
       то необходимо проверить раздел "Список несозданных НМ с ошибками". <br>
    Для того чтобы убрать НМ из ошибочных, необходимо повторно сделать запрос
     с исправленными ошибками.<br>
     Максимальный размер запроса 10 Мб.

     Габариты товаров можно указать только в **сантиметрах**.
    """

    def execute(self, upload_add_data: UploadAddData) -> ResponseCardCreate:
        response = self._post(url=URL, json=to_dict(upload_add_data))
        if response:
            return from_dict(ResponseCardCreate, response)
