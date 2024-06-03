from WB.content.requests.media_files.media_data import MediaFileData
from WB.request_executor import AbsRequestExecutor, SERVER
from WB.content.responses.media_files.response_media import ResponseMedia
from WB.serializers import from_dict

URL = f"{SERVER}'/content/v3/media/file'"


class RequestMediaFileAPI(AbsRequestExecutor):
    """
    **Изменить медиафайлы**

    Добавляет один медиафайл для товара (номенклатуры).

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

    def execute(
        self,
        media_file_data: MediaFileData,
        x_nm_id: int,
        x_photo_number: int
    ) -> ResponseMedia:
        """
        :param x_nm_id: Артикул Wildberries
        :param x_photo_number: Номер медиафайла на загрузку, начинается с `1`.
         При загрузке видео всегда указывайте `1`.
         Чтобы добавить изображение к уже загруженным, номер медиафайла должен
          быть больше количества уже загруженных медиафайлов.'
        """

        self._add_header("X-Nm-Id", x_nm_id)
        self._add_header("X-Photo-Number", x_nm_id)

        response = self._post(
            url=URL,
            data=media_file_data.uploadfile,
            content_type="multipart/form-data"
        )
        if response:
            return from_dict(ResponseMedia, response)

