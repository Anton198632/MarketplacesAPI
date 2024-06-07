from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass


@dataclass
class ContentV3MediaFileResponse200:
    """
    Добавить медиафайлы
    Добавляет один медиафайл для товара (номенклатуры).
        Требования к изображениям:
          * максимум изображений для одного товара (номенклатуры) — 30;
      * минимальное разрешение – 700 × 900 пикселей;
      * максимальный размер — 32 Мб;
      * минимальное качество — 65%;
      * форматы — JPG, PNG, BMP, GIF (статичные), WebP.
        Требования к видео:
          * максимум 1 видео для одного товара (номенклатуры);
      * максимальный размер — 50 Мб;
      * форматы — MOV, MP4.
    """

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: Optional[Dict]
