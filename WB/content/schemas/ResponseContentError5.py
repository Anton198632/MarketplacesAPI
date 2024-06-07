from typing import Optional
from typing import Dict
from typing import Any
from dataclasses import dataclass
from WB.content.schemas import ResponseContentError5AdditionalErrors


@dataclass
class ResponseContentError5:

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
    #  Дополнительные ошибки
    additionalErrors: ResponseContentError5AdditionalErrors
