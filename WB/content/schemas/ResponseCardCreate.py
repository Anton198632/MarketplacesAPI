from typing import Optional
from types import NoneType
from typing import Any
from typing import Dict
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
