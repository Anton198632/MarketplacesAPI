from typing import Optional
from typing import Any
from WB.content.schemas import ResponseContentError5AdditionalErrors
from typing import Dict
from dataclasses import dataclass


@dataclass
class ResponseContentError5:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    AdditionalErrors: ResponseContentError5AdditionalErrors
