from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class ErrorWrongParameters:
    """
    Неправильный запрос

    
    """

    data: Optional[Dict]

    error: bool

    errorText: str
