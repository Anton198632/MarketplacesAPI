from typing import Optional
from typing import Any
from WB.content.schemas import ResponseBodyContentError400AdditionalErrors
from typing import Dict
from dataclasses import dataclass


@dataclass
class ResponseBodyContentError400:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    AdditionalErrors: ResponseBodyContentError400AdditionalErrors
