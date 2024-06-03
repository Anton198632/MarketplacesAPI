from dataclasses import dataclass, field
from typing import List, Any, Optional

from WB.content.responses.response import Response
from WB.content.responses.tag import Tag


@dataclass
class ResponseTags(Response):
    data: List[Tag] = field(
        default=list, metadata={"description": "Тэги продавца"}
    )


@dataclass
class ResponseTag(Response):
    data: Optional[Any] = field(default=None)
