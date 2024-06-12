import inspect
import re
from dataclasses import fields, dataclass
from typing import Type


def build_parameters_for_url(url, function):
    pattern = r'\{([^}]+)\}'
    path_parameters = re.findall(pattern, url)

    frame = inspect.currentframe().f_back
    local_vars = frame.f_locals
    first_function_signature = inspect.signature(function)
    parameters = []
    for param_name, param in first_function_signature.parameters.items():
        if param_name != "body_request" and param_name not in path_parameters:
            param_value = local_vars[param_name]
            if param_value:
                parameters.append(f"{param_name}={param_value}")

    for path_parameter in path_parameters:
        param_value = local_vars[path_parameter]
        if param_value:
            url = url.replace(f"{{{path_parameter}}}", str(param_value))

    return f'{url}?{"&".join(parameters)}'


def is_xx_status(status_code, first_number):
    re_word = rf"^{first_number}\d\d$"
    return bool(re.match(re_word, str(status_code)))


def create_combined_dataclass(class_name: str, *bases: Type):
    # Сбор всех полей из базовых классов
    combined_fields = []
    for base in bases:
        if hasattr(base, '__dataclass_fields__'):
            combined_fields.extend(fields(base))

    # Создание нового класса с объединенными полями
    @dataclass
    class Combined(*bases):
        def __post_init__(self):
            # Вызываем __post_init__ для каждого базового класса
            for base in bases:
                base_init = getattr(base, '__post_init__', None)
                if base_init is not None:
                    base_init(self)

    # Добавление полей в класс
    for field in combined_fields:
        setattr(Combined, field.name,
                field.default if field.default != field.default_factory else field.default_factory)

    Combined.__name__ = class_name
    return Combined