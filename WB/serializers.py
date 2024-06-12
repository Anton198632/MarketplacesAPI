from dataclasses import asdict
from typing import TypeVar, Type, Any, Union, List

import dacite
from requests import Response

T = TypeVar('T')


def from_response(
        data_class: Union[Type[T], List[Type[T]]], response: Response
):
    if not isinstance(data_class, list):
        data_class = [data_class]

    content_type = response.headers.get("Content-Type")
    if "application/json" in content_type:
        for d_class in data_class:
            try:
                return from_dict(d_class, response.json())
            except:
                pass
    elif "text/plain" in content_type:
        return response.text
    else:
        pass


def from_dict(data_class: Type[T], data: Any) -> T:
    return dacite.from_dict(data_class=data_class, data=data)


def to_dict(data: Any):
    return asdict(data)
