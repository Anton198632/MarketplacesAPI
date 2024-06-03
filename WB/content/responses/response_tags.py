from dataclasses import dataclass, field
from typing import List, Any, Optional

from WB.content.responses.response import Response


@dataclass
class Tag:
    id: int = field(metadata={"description": "Числовой идентификатор тега"})
    color: str = field(metadata={"description": "Цвет тега"})
    name: str = field(metadata={"description": "Имя тега"})


@dataclass
class ResponseTags(Response):
    data: List[Tag] = field(
        default=list, metadata={"description": "Тэги продавца"}
    )


@dataclass
class ResponseTag(Response):
    data: Optional[Any] = field(default=None)
