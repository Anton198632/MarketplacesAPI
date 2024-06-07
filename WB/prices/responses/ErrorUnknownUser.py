from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class ErrorUnknownUser:
    """
    Ошибка авторизации

    
    """

    data: Optional[Dict]

    error: bool

    errorText: str
