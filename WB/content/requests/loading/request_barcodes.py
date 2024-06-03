from WB.content.requests.loading.barcodes_data import BarcodesData
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.loading.response_barcodes import ResponseBarcodes
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v2/barcodes"


class RequestBarcodesAPI(AbsRequestExecutor):
    """
    **Генерация баркодов**

    Метод позволяет сгенерировать массив уникальных баркодов для создания
     размера НМ в КТ.
    """

    def execute(self, barcodes_data: BarcodesData) -> ResponseBarcodes:
        response = self._post(url=URL, json=to_dict(barcodes_data))
        if response:
            return from_dict(ResponseBarcodes, response)
