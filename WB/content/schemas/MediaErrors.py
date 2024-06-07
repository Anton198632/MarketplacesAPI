from typing import Any
from typing import Dict
from typing import Optional
from dataclasses import dataclass


@dataclass
class MediaErrors:
    #  Дополнительные ошибки
    additionalErrors: Optional[Dict]

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
