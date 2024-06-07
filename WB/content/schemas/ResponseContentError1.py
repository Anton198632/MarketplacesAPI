from typing import Optional
from WB.content.schemas import ResponseContentError1AdditionalErrors
from typing import Any
from typing import Dict
from dataclasses import dataclass


@dataclass
class ResponseContentError1:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    AdditionalErrors: ResponseContentError1AdditionalErrors
