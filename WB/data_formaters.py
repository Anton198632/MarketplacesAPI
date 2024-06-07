import os
from dataclasses import asdict
from typing import Optional, List, Dict

from jinja2 import FileSystemLoader, Environment


def build_class_header(
        title: str = None, description: str = None
) -> Optional[str]:
    if description:
        description = description.replace(" ", " ")
        description = description.replace("\n", "\n    ")
    else:
        description = ""

    header = (
        f'"""\n{title}\n{description}\n"""\n' if title else None
    )
    if header:
        result_header = []
        rows = header.split("\n")
        for row in rows:
            if len(row) > 75:
                row_parts = [
                    row[i: i + 75]
                    for i in range(0, len(row), 75)
                ]
            else:
                row_parts = [row]
            result_header += row_parts
        header = "    " + "\n    ".join(result_header) + "\n"
        header = header.replace("    \n", "").replace("        ", "    ")

    return header


def build_request_class(
        section: str,
        method: str,
        url: str,
        parameters: List,
        responses_classes: Dict,
        body_request_class: Optional[object] = None,
):
    class_name = "".join([f"{u[0].upper()}{u[1:]}" for u in url[1:].split("/")])
    class_name = f"{class_name}{method.capitalize()}"

    imports_responses_classes = []
    for key, response_class in responses_classes.items():
        responses_path = "responses"
        if not os.path.exists(
            f"WB/{section}/{responses_path}/{response_class}.py"
        ):
            responses_path = "schemas"
        imports_responses_classes.append(
            f"from WB.{section}.{responses_path} import {response_class}"
        )

    body_request_json_row = (
        f"    json=asdict(body_request, {body_request_class})"
        if body_request_class else ""
    )

    parameters = [f"{p}: str" for p in parameters]
    if body_request_class:
        parameters.append(f"body_request: {body_request_class}")

    class_data = {
        "imports": [
            "import requests",
            "from dataclasses import asdict"
            "from WB.create_logger import create_logger",

            f"from WB.{section}.requestBodies import {body_request_class}"
            if body_request_class else "",

            *imports_responses_classes,
        ],
        "constants": {
            "SERVER": "https://suppliers-api.wildberries.ru",
            "URL": url,

        },
        "classes": {
            class_name: {
                "attributes": {
                    "api_key": "str",
                },
                "methods": {
                    "execute": {
                        "params": [
                            "self",
                            *parameters
                        ],
                        "body": [
                            f"response = requests.{method}(",
                            f'    url="{url}"',
                            body_request_json_row,
                            f")"
                        ]
                    }
                }
            },
        }
    }

    # Настройка Jinja2
    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)

    # Загрузка шаблона
    template = env.get_template('WB/request_template.j2')

    # Генерация кода
    output = template.render(
        imports=class_data['imports'],
        constants=class_data['constants'],
        classes=class_data['classes']
    )

    pass