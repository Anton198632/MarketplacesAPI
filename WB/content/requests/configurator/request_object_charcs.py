from typing import Optional

from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.configurator.response_object_charcs import ResponseObjectCharcs

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/object/charcs/"


class RequestObjectCharcsAPI(AbsRequestExecutor):
    """
    **Характеристики предмета (подкатегории)**

    Получение списка характеристик предмета по его ID.
    """

    def execute(
        self, subjectId: int, locale: Optional[str]
    ) -> ResponseObjectCharcs:
        """
        :param locale: Example: locale=ru
         Язык для перевода полей ответа name, value и object: ru - русский,
          en - английский, zh - китайский.
          Не используется в песочнице.
        """
        url = f"{URL}{subjectId}?{locale=}" if locale else URL
        response = self._get(url)
        if response:
            return from_dict(ResponseObjectCharcs, response)
