import json
import os
from typing import Dict, Optional

from WB.data_formaters import replace_key_words_and_symbols


def dict_write(filename: str, data: Dict) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def build_path(path: str) -> str:
    path = replace_key_words_and_symbols(path)
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
    path = replace_key_words_and_symbols(path)
    build_path(path)

    filename = f"{path}/{class_.__name__}.py"
    with open(filename, 'w', encoding="utf-8") as file:

        # Запись импортов
        for imp in imports:
            row = f"{imp}\n"
            if "CLASS" in imp:
                import_class_name = imp.split(" ")[-1].replace(".", "")
                row = row.replace("CLASS", import_class_name)
                row = replace_key_words_and_symbols(row)
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
    path = replace_key_words_and_symbols(path)
    build_path(path)
    filename = f"{path}/{name}.py"

    with open(filename, 'w', encoding="utf-8") as file:
        # Запись импортов
        for imp in imports:
            row = f"{imp}\n"
            if "CLASS" in imp:
                import_class_name = imp.split(" ")[-1].replace(".", "")
                row = row.replace("CLASS", import_class_name)
                pass

            file.write(row)

        # for class_ in classes:
        #     header_text = f"    {header}\n" if header else ""
        #     file.write(
        #         f"\n\n@dataclass\n"
        #         f'class {class_.get("class_name")}'
        #         f'({class_.get("base_class")}):\n'
        #         f"{header_text}"
        #         '    pass\n'
        #     )

        for class_ in classes:
            header_text = f"    {header}\n" if header else ""
            file.write(
                f"\n{header_text}"
                f'{class_.get("class_name")} = {class_.get("base_class")}\n'
            )