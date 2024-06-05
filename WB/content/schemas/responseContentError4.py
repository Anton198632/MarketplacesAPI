from typing import Optional
from typing import Dict
from WB.content.schemas import responseContentError4Additionalerrors
from typing import Any
from dataclasses import dataclass


@dataclass
class responseContentError4:
    data: Optional[Dict]
    error: bool
    errorText: str
    additionalErrors: responseContentError4Additionalerrors
