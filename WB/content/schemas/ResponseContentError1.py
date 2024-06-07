from typing import Optional
from typing import Dict
from typing import Any
from WB.content.schemas import ResponseContentError1AdditionalErrors
from dataclasses import dataclass


@dataclass
class ResponseContentError1:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: ResponseContentError1AdditionalErrors
