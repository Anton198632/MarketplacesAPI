from typing import Any
from typing import Optional
from dataclasses import dataclass
from typing import Dict


@dataclass
class mediaErrors:
    additionalErrors: Optional[Dict]
    data: Optional[Dict]
    error: bool
    errorText: str
