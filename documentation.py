def generate_documentation(dataclass_type):
    documentation = []
    for field_name, field_info in dataclass_type.__dataclass_fields__.items():
        desc = field_info.metadata.get(
            "description", "No description provided"
        )
        documentation.append(f"{field_name}: {desc}")
        if hasattr(field_info.type, '__dataclass_fields__'):
            sub_doc = generate_documentation(field_info.type)
            for line in sub_doc:
                documentation.append(f"  {line}")
    return documentation
