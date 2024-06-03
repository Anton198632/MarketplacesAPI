from dataclasses import dataclass, field
from typing import List

from WB.content.responses.response import Response


@dataclass
class ResponseBarcodes(Response):
    data: List[str] = field(
        default=[],
        metadata={"description": "Массив сгенерированных баркодов"},
    )
