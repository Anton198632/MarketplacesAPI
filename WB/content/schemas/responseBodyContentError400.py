from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass
from WB.content.schemas import responseBodyContentError400Additionalerrors


@dataclass
class responseBodyContentError400:
    data: Optional[Dict]
    error: bool
    errorText: str
    additionalErrors: responseBodyContentError400Additionalerrors
