from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.requests.tags.tag_data import TagNomenclatureData
from WB.content.responses.tags.response_tags import ResponseTag
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/tag/nomenclature/link"


class RequestTagNomenclatureLinkAPI(AbsRequestExecutor):
    """
    **Управление тегами в КТ**

    Метод позволяет добавить теги к КТ и снять их с КТ.
     При снятии тега с КТ сам тег не удаляется.
     К карточке можно добавить 15 тегов.
    """

    def execute(
        self, tag_nomenclature_data: TagNomenclatureData
    ) -> ResponseTag:
        response = self._post(url=URL, json=to_dict(tag_nomenclature_data))
        if response:
            return from_dict(ResponseTag, response)
