from WB.content.requests.media_files.media_data import MediaSaveData
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.media_files.response_media import ResponseMedia
from WB.serializers import to_dict, from_dict

URL = f"{SERVER}/content/v3/media/save"


class RequestMediaSaveAPI(AbsRequestExecutor):
    """
    **Изменить медиафайлы**

    Изменяет набор медиафайлов для товара (номенклатуры).
    **Внимание**. Новые медиафайлы (`data`) полностью заменяют старые
     (`mediaFiles`). Чтобы добавить новые медиафайлы,
      укажите ссылки не только на них, но и на старые файлы.

    Требования к изображениям:
      * максимум изображений для одного товара (номенклатуры) — 30;
        * минимальное разрешение – 700 × 900 пикселей;
          * максимальный размер — 32 Мб;
            * минимальное качество — 65%;
              * форматы — JPG, PNG, BMP, GIF (статичные), WebP.

    Требования к видео:
    * максимум 1 видео для одного товара (номенклатуры).
      * максимальный размер — 50 Мб;
        * форматы — MOV, MP4.

    Если хотя бы одно изображение в запросе не соответствует требованиям, то
     даже при успешном ответе (200) ни одно изображение не загрузится
    """

    def execute(self, media_save_data: MediaSaveData) -> ResponseMedia:
        response = self._post(url=URL, json=to_dict(media_save_data))
        if response:
            return from_dict(ResponseMedia, response)
