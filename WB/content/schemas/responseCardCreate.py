from typing import Optional
from typing import Dict
from types import NoneType
from typing import Any
from dataclasses import dataclass


@dataclass
class responseCardCreate:
    data: Optional[Dict]
    error: bool
    errorText: str
    additionalErrors: NoneType
