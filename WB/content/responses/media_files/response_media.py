from dataclasses import dataclass, field
from typing import Any

from WB.content.responses.response import Response


@dataclass
class ResponseMedia(Response):
    data: Any = field(default={})
