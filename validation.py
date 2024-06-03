from dataclasses import MISSING


def validate_data(instance):
    for field_name, field_info in instance.__dataclass_fields__.items():
        value = getattr(instance, field_name)
        if value is None:
            if (
                field_info.default is MISSING
                and field_info.default_factory is MISSING
            ):
                raise ValueError(f"Field '{field_name}' is required.")
        if hasattr(value, '__dataclass_fields__'):
            validate_data(value)
        elif isinstance(value, list) and value and hasattr(
                value[0], '__dataclass_fields__'
        ):
            for item in value:
                validate_data(item)
