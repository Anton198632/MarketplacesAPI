from dataclasses import dataclass, field
from typing import List, Optional

from WB.content.responses.response import Response


@dataclass
class Subcategory:
    subjectID: Optional[int] = field(
        default=None, metadata={"description": "Идентификатор предмета"}
    )
    parentID: Optional[int] = field(
        default=None,
        metadata={"description": "Идентификатор родительской категории"},
    )
    subjectName: Optional[str] = field(
        default=None, metadata={"description": "Название предмета"}
    )
    parentName: Optional[str] = field(
        default=None,
        metadata={"description": "Название родительской категории"},
    )


@dataclass
class ResponseObjectAll(Response):
    data: List[Subcategory] = field(
        default_factory=list,
        metadata={"description": "Подкатегории (предметы)"},
    )
