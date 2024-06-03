from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.requests.tags.tag_data import TagData
from WB.content.responses.tags.response_tags import ResponseTag
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/tag"


class RequestCreateTagAPI(AbsRequestExecutor):
    """
    **Создание тега**

    Метод позволяет создать тег.<br> Завести можно 15 тегов.<br> Максимальная
     длина тега 15 символов.
    """

    def execute(self, tag_data: TagData) -> ResponseTag:
        response = self._post(url=URL, json=to_dict(tag_data))
        if response:
            return from_dict(ResponseTag, response)


class RequestUpdateTagAPI(AbsRequestExecutor):
    """
    **Изменение тега**

    Метод позволяет изменять информацию о теге (имя и цвет).
    """

    def execute(self, tag_id: int, tag_data: TagData) -> ResponseTag:
        response = self._patch(url=f"{URL}/{tag_id}", json=to_dict(tag_data))
        if response:
            return from_dict(ResponseTag, response)


class RequestDeleteTagAPI(AbsRequestExecutor):
    """
    **Удаление тега**

    Метод позволяет удалить тег
    """

    def execute(self, tag_id: int) -> ResponseTag:
        response = self._delete(url=f"{URL}/{tag_id}")
        if response:
            return from_dict(ResponseTag, response)

