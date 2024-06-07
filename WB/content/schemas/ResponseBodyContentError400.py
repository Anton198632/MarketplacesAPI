from typing import Optional
from typing import Dict
from WB.content.schemas import ResponseBodyContentError400AdditionalErrors
from typing import Any
from dataclasses import dataclass


@dataclass
class ResponseBodyContentError400:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: ResponseBodyContentError400AdditionalErrors
