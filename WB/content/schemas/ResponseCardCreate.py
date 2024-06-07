from typing import Optional
from typing import Dict
from typing import Any
from types import NoneType
from dataclasses import dataclass


@dataclass
class ResponseCardCreate:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: NoneType
