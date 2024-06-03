from dataclasses import dataclass, field
from typing import List, Optional

from WB.content.responses.response import Response


@dataclass
class Tnved:
    tnved: Optional[str] = field(
        default=None, metadata={"description": "ТНВЭД-код"}
    )
    isKiz: Optional[bool] = field(
        default=None,
        metadata={
            "description": (
                "- `true` - код маркировки требуется\n"
                "- `false` - код маркировки не требуется"
            ),
        },
    )


@dataclass
class ResponseDirectoryTnved(Response):
    data: List[Tnved] = field(
        default_factory=list, metadata={"description": "Данные"}
    )
