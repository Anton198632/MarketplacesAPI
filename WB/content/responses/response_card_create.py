from dataclasses import dataclass, field

from WB.content.responses.response import Response


@dataclass
class ResponseCardCreate(Response):
    data: None = field(default=None)
