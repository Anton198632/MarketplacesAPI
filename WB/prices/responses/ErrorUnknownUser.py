from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass


@dataclass
class ErrorUnknownUser:
    """
    Ошибка авторизации
    """

    data: Optional[Dict]

    error: bool

    errorText: str
