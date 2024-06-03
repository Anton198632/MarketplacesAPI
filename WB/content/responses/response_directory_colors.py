from dataclasses import dataclass, field
from typing import Optional

from WB.content.responses.response import Response


@dataclass
class Item:
    name: Optional[str] = field(
        default=None, metadata={"description": "Наименование цвета"}
    )
    parentName: Optional[str] = field(
        default=None,
        metadata={"description": "Наименование родительского цвета"},
    )


@dataclass
class ResponseDirectoryColor(Response):
    data: Optional[Item] = field(
        default=None,
        metadata={"description": "Объект с информацией о цветах"},
    )
