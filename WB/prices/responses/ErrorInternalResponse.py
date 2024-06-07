from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass


@dataclass
class ErrorInternalResponse:
    """
    Прочие ошибки
    """

    data: Optional[Dict]

    error: bool

    errorText: str
