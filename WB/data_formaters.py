import os
import re
from dataclasses import asdict
from typing import Optional, List, Dict

from jinja2 import FileSystemLoader, Environment


def build_class_header(
        title: Optional[str] = None, description: str = None
) -> Optional[str]:
    if description:
        description = description.replace(" ", " ")
        description = description.replace("\n", "\n    ")
    else:
        description = ""

    if title:
        title = title.replace(" ", " ")
        title = title.replace("\n", "\n    ")

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
        description: str,
        body_request_class: Optional[dict] = None,
):
    class_name = "".join(
        [f"{u[0].upper()}{u[1:]}" for u in url[1:].split("/")]
    )

    if "{" in class_name:
        cl_n_parts = re.split(r"[{}]", class_name)
        class_name = "".join(
            [f"{cl[0].upper()}{cl[1:]}" if cl else "" for cl in cl_n_parts]
        )

    class_name = f"{class_name}{method.capitalize()}"

    imports_responses_classes = []
    responses_handler_rows = []
    for key, response_class in responses_classes.items():
        imports_responses_classes.append(
            f'from {response_class.get("import")}'
            f' import {response_class.get("class")}'
        )

        if "X" in key:
            responses_handler_rows += [
                f"if is_xx_status(response.status_code, {str(key)[0]}):",
            ]
        else:
            responses_handler_rows += [f"if response.status_code == {key}:"]
        responses_handler_rows += [
            f'    return from_response({response_class.get("class")},'
            f' response)',
        ]

    body_request_json_row = (
        "    json=asdict(body_request)" if body_request_class else ""
    )
    headers = '    headers={"Authorization": self.api_key},'

    if len(parameters) > 0:
        for parameter in parameters:
            if parameter.get("in") != "query":
                pass
        pass

    parameters_ = [
        (
            f'{p.get("name")}: {p.get("type")}'
            f'{f" = None" if not p.get("required") else ""}'
        )
        if p.get("in") == "query" else ""
        for p in parameters
    ]



    if body_request_class:
        parameters_.append(f'body_request: {body_request_class.get("class")}')

    class_data = {
        "imports": [

            "from dataclasses import asdict",
            "import requests",
            "from WB.create_logger import create_logger",
            "from WB.serializers import from_response",
            "from WB.utils import build_parameters_for_url, is_xx_status",

            (
                f'from {body_request_class.get("import")}'
                f'.{body_request_class.get("class")}'
                f' import {body_request_class.get("class")}'
            )
            if body_request_class else "",

            *imports_responses_classes,
        ],
        "constants": {
            "SERVER": "https://suppliers-api.wildberries.ru",
            "URL": url,

        },
        "classes": {
            class_name: {
                "description": description,
                "attributes": {
                    "api_key": "str",
                },
                "methods": {
                    "execute": {
                        "params": [
                            "self",
                            *parameters_
                        ],
                        "body": [
                            f"url = build_parameters_for_url(URL,"
                            f" self.execute)",

                            f"response = requests.{method}(",
                            '    url=f"{SERVER}{url}",',
                            headers,
                            body_request_json_row,
                            f")",
                            *responses_handler_rows,
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

    with open(f"WB/{section}/{class_name}.py", "w", encoding="utf-8") as f:
        f.write(output)

    pass
