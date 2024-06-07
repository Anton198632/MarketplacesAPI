from typing import Any
from dataclasses import dataclass
from typing import Optional
from typing import Dict


@dataclass
class ResponseBodyContentError403:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: str
