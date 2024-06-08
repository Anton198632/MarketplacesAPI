import json
import os
from typing import Dict, Optional, Union


def dict_write(filename: str, data: Dict) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_path(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def write_class_to_script(
    path: str,
    class_: type,
    imports: set,
    annotations: dict,
    descriptions: Optional[dict] = None,
    header: Optional[str] = None
):
    # Запись в файл-скрипт
    filename = f"{path}/{class_.__name__}.py"
    with open(filename, 'w', encoding="utf-8") as file:

        # Запись импортов
        for imp in imports:
            if len(imp) > 79:
                begin = imp[0:imp.rfind(" ")]
                end = imp[imp.rfind(" ") + 1:]
                imp = f"{begin} (\n    {end},\n)"
            file.write(f"{imp}\n")
        file.write("\n\n")

        # Запись определения класса
        file.write(f"@dataclass\n")
        file.write(f"class {class_.__name__}:\n")

        if header:
            file.write(header)

        for field_name, field_annotation in annotations.items():
            if hasattr(field_annotation, "__origin__"):
                if field_annotation.__origin__ is Union and type(
                        None) in field_annotation.__args__:
                    non_none_args = [arg for arg in
                                     field_annotation.__args__ if
                                     arg is not type(None)]
                    annotation_str = (
                        f"Optional[{non_none_args[0].__name__}]"
                    )
                elif field_annotation.__origin__ is list:
                    annotation_str = (
                        f"{field_annotation.__name__}"
                        f"[{field_annotation.__args__[0].__name__}]"
                    )
                else:
                    args = ", ".join(
                        arg.__name__ for arg in field_annotation.__args__
                    )
                    annotation_str = (
                        f"{field_annotation.__origin__.__name__}[{args}]"
                    )

            elif field_annotation:
                annotation_str = field_annotation.__name__
            else:
                annotation_str = None

            description = (
                descriptions[field_name]
                if descriptions and descriptions.get(field_name)
                else ""
            )

            description = (
                description.strip()
                .replace("<br>", "")
                .replace(" ", " ")
            )

            description_rows = [
                description[i : i+72]
                for i in range(0, len(description), 72)
            ]

            description_rows_result = []
            for description_row in description_rows:
                d_rows = description_row.split("\n")
                description_rows_result += [
                    f"    #  {d}" for d in d_rows
                ]
            description = "\n".join(description_rows_result)

            file.write(f"{description}\n")
            file.write(
                f"    {field_name}: {annotation_str}\n"
            )


def write_const_to_scripts(
        path: str, name: str, imports: set, data: str
):
    # Запись в файл-скрипт
    name = f"{name[0].upper()}{name[1:]}"
    filename = f"{path}/{name}.py"
    with open(filename, 'w', encoding="utf-8") as file:
        # Запись импортов
        for imp in imports:
            if len(imp) > 79:
                begin = imp[0:imp.rfind(" ")]
                end = imp[imp.rfind(" ") + 1]
                imp = f"{begin} (\n    {end},\n)"
            file.write(f"{imp}\n")
        file.write("\n\n")

        file.write(data)