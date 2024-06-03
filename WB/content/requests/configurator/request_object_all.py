from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_object_all import ResponseObjectAll

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/object/all"


class RequestObjectAllAPI(AbsRequestExecutor):
    """
    **Список предметов (подкатегорий)**

    С помощью данного метода можно получить список всех доступных предметов,
     родительских категорий предметов, и их идентификаторов.
    """

    def execute(
        self,
        name: Optional[str],
        limit: Optional[int],
        locale: Optional[str],
        offset: Optional[int],
        parentID: Optional[int],
    ) -> ResponseObjectAll:
        """
        :param name: Поиск по наименованию предмета (Носки), поиск работает
         по подстроке, искать можно на любом из поддерживаемых языков.
        :param limit: Количество подкатегорий (предметов), максимум 1 000
        :param locale: Язык полей ответа (ru, en, zh).
        Не используется в песочнице
        :param offset: Номер позиции, с которой необходимо получить ответ
        :param parentID: 'Идентификатор родительской категории предмета
        :return:
        """

        params = []
        if locale:
            params.append(f"{locale=}")
        if name:
            params.append(f"{name=}")
        if limit:
            params.append(f"{limit=}")
        if offset:
            params.append(f"{offset=}")
        if parentID:
            params.append(f"{parentID}")
        url = f"{URL}?{'&'.join(params)}"
        response = self._get(url)
        if response:
            return from_dict(ResponseObjectAll, response)
