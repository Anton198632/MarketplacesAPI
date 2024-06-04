from dataclasses import asdict
from typing import TypeVar, Type, Any

import dacite

T = TypeVar('T')


def from_dict(data_class: Type[T], data: Any) -> T:
    return dacite.from_dict(data_class=data_class, data=data)


def to_dict(data: Any):
    return asdict(data)
