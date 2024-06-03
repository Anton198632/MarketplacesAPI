from dataclasses import dataclass, field
from typing import Any, Optional, Dict


@dataclass
class Response:
    data: Optional[Any] = field(default=None)
    error: bool = field(default=False, metadata={"description": "Флаг ошибки"})
    errorText: str = field(
        default="", metadata={"description": "Описание ошибки"}
    )
    additionalErrors: Dict = field(
        default={}, metadata={"descriptions": "Дополнительные ошибки"}
    )
