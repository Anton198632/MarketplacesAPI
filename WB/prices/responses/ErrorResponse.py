from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class ErrorResponse:
    """
    Другие ошибки

    
    """

    data: Optional[Dict]

    error: bool

    errorText: str
