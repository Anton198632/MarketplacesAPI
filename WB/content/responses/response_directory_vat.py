from dataclasses import dataclass, field
from typing import List

from WB.content.responses.response import Response


@dataclass
class ResponseDirectoryVat(Response):
    data: List[str] = field(
        default_factory=list, metadata={"description": "Ставка НДС"}
    )

