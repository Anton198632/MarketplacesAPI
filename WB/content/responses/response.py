from dataclasses import dataclass, field
from typing import Any, Optional, Dict, Union


@dataclass
class Response:
    data: Optional[Any] = field(default=None)
    error: bool = field(default=False, metadata={"description": "Флаг ошибки"})
    errorText: str = field(
        default="", metadata={"description": "Описание ошибки"}
    )
    additionalErrors: Union[Dict, str, None] = field(
        default={}, metadata={"descriptions": "Дополнительные ошибки"}
    )
