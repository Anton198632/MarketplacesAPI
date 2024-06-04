from typing import Any
from typing import Dict
from dataclasses import dataclass
from typing import Optional


@dataclass
class ResponseError:
    data: Optional[Dict]
    error: bool
    errorText: Optional[str]
