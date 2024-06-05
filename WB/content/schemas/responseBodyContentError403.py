from typing import Any
from typing import Optional
from dataclasses import dataclass
from typing import Dict


@dataclass
class responseBodyContentError403:
    data: Optional[Dict]
    error: bool
    errorText: str
    additionalErrors: str
