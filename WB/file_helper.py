import json
import os
from typing import Dict, Optional, Union

from WB.data_formaters import build_class_header


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
        header: Optional[str] = None,
):
    # Запись в файл-скрипт
    path = path.replace("{", "").replace("}", "").replace("-", "_")
    build_path(path)

    filename = f"{path}/{class_.__name__}.py"
    with open(filename, 'w', encoding="utf-8") as file:

        # Запись импортов
        for imp in imports:
            # if len(imp) > 79:
            #     begin = imp[0:imp.rfind(" ")]
            #     end = imp[imp.rfind(" ") + 1:]
            #     imp = f"{begin} (\n    {end},\n)"

            row = f"{imp}\n"
            if "CLASS" in imp:
                import_class_name = imp.split(" ")[-1].replace(".", "")
                row = row.replace("CLASS", import_class_name)
                pass

            file.write(row)
        file.write("\n\n")

        # Запись определения класса
        file.write(f"@dataclass\n")
        file.write(f"class {class_.__name__}:\n")

        if header:
            file.write(header)

        annotations_result = []
        for field_name, field_annotation in annotations.items():
            annotation_str = (
                str(field_annotation)
                .replace("typing.", "")
                .replace("WB.parser.", "")
                .replace("<class '", "")
                .replace("'>", "")
            )

            annotations_result.append(
                {
                    "field_name": field_name,
                    "annotation_str": annotation_str,
                    "required": "Optional" not in annotation_str

                }
            )

            # if hasattr(field_annotation, "__origin__"):
            #     if field_annotation.__origin__ is Union and type(
            #             None) in field_annotation.__args__:
            #         non_none_args = [arg for arg in
            #                          field_annotation.__args__ if
            #                          arg is not type(None)]
            #         annotation_str = (
            #             f"Optional[{non_none_args[0].__name__}]"
            #         )
            #     elif field_annotation.__origin__ is list:
            #         annotation_str = (
            #             f"{field_annotation.__name__}"
            #             f"[{field_annotation.__args__[0].__name__}]"
            #         )
            #     else:
            #         args = ", ".join(
            #             arg.__name__ for arg in field_annotation.__args__
            #         )
            #         annotation_str = (
            #             f"{field_annotation.__origin__.__name__}[{args}]"
            #         )
            #
            # elif field_annotation:
            #     annotation_str = field_annotation.__name__
            # else:
            #     annotation_str = None

        annotations_result.sort(key=lambda a: a.get("required"), reverse=True)

        for annot in annotations_result:

            description = (
                descriptions[annot.get("field_name")]
                if descriptions and descriptions.get(annot.get("field_name"))
                else ""
            )

            description = (
                description.strip()
                    .replace("<br>", "")
                    .replace(" ", " ")
            )

            description_rows = [
                description[i: i + 72]
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
                f'    {annot.get("field_name")}:'
                f' {annot.get("annotation_str")}'
                f'{" = None" if not annot.get("required") else ""}\n'
            )


def write_descendant_class_to_script(
    path: str,
    name: str,
    imports: set,
    classes: list,
    header: Optional[str] = None,
):
    # Запись в файл-скрипт
    name = f"{name[0].upper()}{name[1:]}".replace("-", "_")
    path = path.replace("{", "").replace("}", "").replace("-", "_")
    build_path(path)
    filename = f"{path}/{name}.py"

    with open(filename, 'w', encoding="utf-8") as file:
        # Запись импортов
        for imp in imports:
            # if len(imp) > 79:
            #     begin = imp[0:imp.rfind(" ")]
            #     end = imp[imp.rfind(" ") + 1]
            #     imp = f"{begin} (\n    {end},\n)"
            row = f"{imp}\n"
            if "CLASS" in imp:
                import_class_name = imp.split(" ")[-1].replace(".", "")
                row = row.replace("CLASS", import_class_name)
                pass

            file.write(row)

        for class_ in classes:
            header_text = f"    {header}\n" if header else ""
            file.write(
                f"\n\n@dataclass\n"
                f'class {class_.get("class_name")}'
                f'({class_.get("base_class")}):\n'
                f"{header_text}"
                '    pass\n'
            )
