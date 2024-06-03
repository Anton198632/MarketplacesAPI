from dataclasses import field, dataclass
from typing import Optional, List

from WB.content.requests.characteristic import Characteristic
from WB.content.requests.dimensions import Dimensions
from WB.content.requests.size import Size


@dataclass
class Card:
    vendorCode: str = field(metadata={"description": "Артикул продавца"})
    brand: Optional[str] = field(
        default=None, metadata={"description": "Бренд"}
    )
    title: Optional[str] = field(
        default=None, metadata={"description": "Наименование товара"}
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "description": (
                "Описание товара. Максимальное количество символов зависит от"
                " категории товара. Стандарт — 2000, минимум — 1000,"
                " максимум — 5000."
            ),
        }
    )
    dimensions: Optional[Dimensions] = field(
        default=None,
        metadata={
            "description": (
                "Габариты упаковки товара. Указывать в сантиметрах для любого"
                " товара. Если не указать структуру dimensions в запросе, то"
                " она сгенерируется системой автоматически с нулевыми"
                " значениями длины, ширины, высоты"
            ),
        }
    )
    sizes: Optional[List[Size]] = field(
        default_factory=list,
        metadata={
            "description": (
                "Массив с размерами. Если для размерного товара (обувь, одежда"
                " и др.) не указать этот массив, то системой в карточке он"
                " будет сгенерирован автоматически с techSize = 'A'"
                " и wbSize = '1' и баркодом."
            ),
        }
    )
    characteristics: Optional[List[Characteristic]] = field(
        default_factory=list,
        metadata={"description": "Массив характеристик товара"},
    )
