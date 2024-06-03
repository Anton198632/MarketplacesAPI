from dataclasses import dataclass, field
from typing import Optional, List

from WB.content.responses.characteristic import Characteristic
from WB.content.responses.dimension import Dimension
from WB.content.responses.photo import Photo
from WB.content.responses.size import Size


@dataclass
class Card:
    nmID: Optional[int] = field(
        default=None, metadata={"description": "Артикул WB"}
    )
    subjectID: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор предмета"}
    )
    vendorCode: Optional[str] = field(
        default=None, metadata={"description": "Артикул продавца"}
    )
    subjectName: Optional[str] = field(
        default=None, metadata={"description": "Название предмета"}
    )
    photos: List[Photo] = field(
        default_factory=list, metadata={"description": "Массив фото"}
    )
    video: Optional[str] = field(
        default=None, metadata={"description": "URL видео"}
    )
    dimensions: Optional[Dimension] = field(
        default=None, metadata={"description": "Габариты упаковки товара, см"}
    )
    characteristics: List[Characteristic] = field(
        default_factory=list, metadata={"description": "Характеристики"}
    )
    sizes: List[Size] = field(
        default_factory=list, metadata={"description": "Размеры товара"}
    )
    createdAt: Optional[str] = field(
        default=None, metadata={"description": "Дата создания"}
    )
