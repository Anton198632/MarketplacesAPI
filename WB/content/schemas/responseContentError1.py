from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass
from WB.content.schemas import responseContentError1Additionalerrors


@dataclass
class responseContentError1:
    data: Optional[Dict]
    error: bool
    errorText: str
    additionalErrors: responseContentError1Additionalerrors
