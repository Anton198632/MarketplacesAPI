from dataclasses import dataclass, field
from typing import Optional

from WB.content.responses.response import Response


@dataclass
class Item:
    name: Optional[str] = field(
        default=None, metadata={"description": "Название категории"}
    )
    id: Optional[int] = field(
        default=None,
        metadata={"description": "Идентификатор родительской категории"},
    )
    isVisible: Optional[bool] = field(
        default=None, metadata={"description": "Виден на сайте"}
    )


@dataclass
class ResponseObjectParentAll(Response):
    data: Optional[Item] = field(
        default=None,
        metadata={"description": "Объект с информацией о категории"},
    )
