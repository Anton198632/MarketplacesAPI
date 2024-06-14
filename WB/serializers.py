from dataclasses import asdict
from typing import TypeVar, Type, Any, Union, List, Optional

import dacite
from requests import Response

T = TypeVar('T')


# Функция для конвертации строки в целое число
def str_to_optional_int(value: Optional[str]) -> Optional[int]:
    return int(value) if value is not None else None


# Конфигурация для dacite
config = dacite.Config(
    type_hooks={
        Optional[int]: str_to_optional_int
    }
)


def from_response(
        data_class: Union[Type[T], List[Type[T]]], response: Response
):
    if not isinstance(data_class, list):
        data_class = [data_class]

    content_type = response.headers.get("Content-Type")
    if "application/json" in content_type:
        for d_class in data_class:
            try:
                r_json = response.json()
                return from_dict(d_class, r_json)
            except Exception as ex:
                pass
    elif "text/plain" in content_type:
        return response.text
    else:
        pass


def from_dict(data_class: Type[T], data: Any) -> T:
    return dacite.from_dict(data_class=data_class, data=data, config=config)


def to_dict(data: Any):
    return asdict(data)
