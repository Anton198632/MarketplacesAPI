from typing import Any
from dataclasses import dataclass
from typing import Optional
from typing import Dict


@dataclass
class MediaErrors:
    #  Дополнительные ошибки
    additionalErrors: Optional[Dict]

    data: Optional[Dict]
    #  Флаг ошибки
    error: bool
    #  Описание ошибки
    errorText: str
