# Универсальная функция для преобразования JSON в dataclass
from dataclasses import asdict
from typing import TypeVar, Type, Any

T = TypeVar('T')


def from_dict(data_class: Type[T], data: Any) -> T:
    if isinstance(data, list):
        return [from_dict(data_class, item) for item in data]  # type: ignore
    if isinstance(data, dict):
        fieldtypes = {
            f.name: f.type for f in data_class.__dataclass_fields__.values()
        }
        return data_class(
            **{f: from_dict(fieldtypes[f], data[f]) for f in data}
        )  # type: ignore
    return data


def to_dict(data: Any):
    return asdict(data)
