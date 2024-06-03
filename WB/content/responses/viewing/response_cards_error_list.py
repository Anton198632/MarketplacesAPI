from dataclasses import dataclass, field
from typing import Optional, List

from WB.content.responses.response import Response


@dataclass
class CardError:
    object: Optional[str] = field(
        default=None,
        metadata={
            "description": "Категория для который создавалось КТ с данной НМ",
        }
    )
    vendorCode: Optional[str] = field(
        default=None, metadata={"description": "Артикул продавца"}
    )
    updateAt: Optional[str] = field(
        default=None, metadata={
            "description": "Дата и время запроса на создание КТ с данным НМ",
        }
    )
    errors: List[str] = field(
        default_factory=list,
        metadata={
            "description": (
                "Список ошибок из-за которых не обработался запрос на создание"
                " КТ с данным НМ"
            )
        }
    )
    objectID: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор предмета"}
    )


@dataclass
class ResponseCardsErrorList(Response):
    data: List[CardError] = field(
        default_factory=list, metadata={"description": "Список объектов"}
    )
