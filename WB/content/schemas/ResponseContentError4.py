from typing import Optional
from typing import Dict
from typing import Any
from WB.content.schemas import ResponseContentError4AdditionalErrors
from dataclasses import dataclass


@dataclass
class ResponseContentError4:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: ResponseContentError4AdditionalErrors
