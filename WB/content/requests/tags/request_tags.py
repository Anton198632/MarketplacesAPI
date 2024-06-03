from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.tags.response_tags import ResponseTags

from WB.serializers import from_dict

URL = f"{SERVER}/content/v2/tags"


class RequestTagsAPI(AbsRequestExecutor):
    """
    **Список тегов**

    Метод позволяет получить список существующих тегов продавца.
    """

    def execute(self) -> ResponseTags:
        response = self._get(URL)
        if response:
            return from_dict(ResponseTags, response)
