from typing import Union

from WB.content.requests.loading.cards_move_nm_data import (
    NMIDJoinData,
    NMIDSplitData,
)

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.response import Response
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/cards/moveNm"


class RequestCardsMoveNmAPI(AbsRequestExecutor):
    """
    **Объединение / Разъединение НМ**

    Метод позволяет объединять номенклатуры (`nmID`) под одним `imtID`
     и разъединять их.<br>

    Для объединения НМ необходимо отправить запрос со списком НМ с заполненным
     параметром `targetIMT` в теле запроса.

    При этом все НМ объединятся под `imtID` указанном в `targetIMT`. <br>
    <br>

    Чтобы отсоединить НМ от карточки, необходимо передать эту НМ без параметра
     `targetIMT` в теле запроса.<br>
     При этом для передаваемой НМ создается новый `imtID`. <br>
     Если в запросе на <b>разъединение</b> передается несколько НМ, то все они
      автоматически <b>объединятся</b> под <b>одним</b> новым `imtID`. <br>

    Чтобы присвоить каждой НМ уникальный `imtID` необходимо передавать по одной
     НМ за запрос.
    Для НМ, не участвующих в запросе, никаких изменений не происходит.<br>
    Максимальный размер запроса 10 Мб.<br>
    <br>

    `ВАЖНО:` Объединить можно только номенклатуры с одинаковыми предметами.<br>
    `ВАЖНО:` В одной КТ (под одним `imtID`) не может быть больше 30 номенклатур
     (`nmID`).
    """

    def execute(
            self, nm_id_data: Union[NMIDJoinData, NMIDSplitData]
    ) -> Response:
        response = self._post(url=URL, json=to_dict(nm_id_data))
        if response:
            return from_dict(Response, response)
