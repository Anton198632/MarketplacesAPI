from dataclasses import dataclass, field
from typing import List

from WB.content.responses.response import Response


@dataclass
class ResponseDirectoryKinds(Response):
    data: List[str] = field(
        default_factory=list,
        metadata={"description": "Массив значений для хар-ки Сезон"},
    )
