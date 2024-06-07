from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class ResponseContentError6:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
