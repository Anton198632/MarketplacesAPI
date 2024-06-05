from typing import Optional
from typing import Dict
from WB.content.schemas import responseContentError5Additionalerrors
from typing import Any
from dataclasses import dataclass


@dataclass
class responseContentError5:
    data: Optional[Dict]
    error: bool
    errorText: str
    additionalErrors: responseContentError5Additionalerrors
