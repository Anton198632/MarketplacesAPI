import re
from typing import Optional, List, Dict

from jinja2 import FileSystemLoader, Environment

MAX_SYMBOLS = 79


def convert_type(type_):
    if type_ == "integer":
        type_ = "int"
    elif type_ == "string":
        type_ = "str"
    elif type_ == "boolean":
        type_ = "bool"
    else:
        pass
    return type_


def replace_key_words_and_symbols(text):
    pattern = r'\breturn\b'
    replacement = 'return_'
    result = re.sub(pattern, replacement, text)
    result = result.replace("{", "").replace("}", "").replace("-", "_")
    return result


def split_text_with_newlines(text, max_length):
    def split_line(line, maxlength):
        words = line.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= maxlength:
                if current_line:
                    current_line += " " + word
                else:
                    current_line = word
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines

    # Разделяем текст по символам новой строки
    sections = text.split('\n')
    result_lines = []

    for section in sections:
        result_lines.extend(split_line(section, max_length))

    return result_lines


def build_class_header(
        title: Optional[str] = None, description: str = None
) -> Optional[str]:
    if description:
        description = (
            description.replace(" ", " ")
            .replace("\n", "\n    ")
            .replace("<b>", "")
            .replace("</b>", "")
            .replace("<p>", "")
            .replace("</p>", "")
            .replace("<br>", "")
            .replace("<li>", "")
            .replace("</li>", "")
            .replace("<ul>", "")
            .replace("</ul>", "")
        )
        description = "\n    ".join(
            split_text_with_newlines(description, MAX_SYMBOLS - 4)
        )
    else:
        description = ""

    if title:
        title = title.replace(" ", " ")
        title = title.replace("\n", "\n    ")
        title = "\n    ".join(split_text_with_newlines(title, MAX_SYMBOLS - 4))

    header = (
        f'\n    {title}\n    {description}' if title else None
    )
    if header:
        header = header.replace("    \n", "").replace("        ", "    ")
        header = f'    """{header}\n    """\n'

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

    class_name = f"{class_name}{method.capitalize()}".replace("-", "_")

    imports_responses_classes = []
    responses_handler_rows = []
    for key, response_class in responses_classes.items():
        class_ = response_class.get("class")
        classes = response_class.get("classes")
        if class_:
            imp = replace_key_words_and_symbols(response_class.get("import"))
            imports_responses_classes.append(
                f'from {imp} import {response_class.get("class")}'
            )
        if classes:
            imp = replace_key_words_and_symbols(response_class.get("imports"))
            imports_responses_classes.append(f"from {imp} import {classes}")
            pass

        if "X" in key:
            responses_handler_rows += [
                f"if is_xx_status(response.status_code, {str(key)[0]}):",
            ]
        else:
            responses_handler_rows += [f"if response.status_code == {key}:"]
        responses_handler_rows += [
            f'    return from_response({class_ if class_ else f"[{classes}]"},'
            f' response)',
        ]

    body_request_json_row = (
        "    json=asdict(body_request)" if body_request_class else ""
    )
    headers = '    headers={"Authorization": self.api_key},'

    if len(parameters) > 0:
        for parameter in parameters:
            in_ = parameter.get("in")
            if in_ != "query" and in_ != "path":
                pass

    parameters_ = []

    if body_request_class:
        class_ = body_request_class.get("class")
        classes = body_request_class.get("classes")
        if class_:
            parameters_.append(f"body_request: {class_}")
        if classes:
            parameters_.append(f'body_request: Union[{classes}]')

    parameters_ += [
        (
            f'{p.get("original_name")}: {p.get("type")}'
            f'{f" = None" if not p.get("required") else ""}'
        )
        if p.get("in") == "query" or p.get("in") == "path" else ""
        for p in parameters
    ]

    class_data = {
        "imports": [

            "from dataclasses import asdict" if body_request_class else None,
            "import requests",
            "from WB.serializers import from_response",
            (
                "from WB.utils import build_parameters_for_url" +
                (
                    ", is_xx_status"
                    if any("X" in key for key in responses_classes.keys())
                    else ""
                )
            ),
            (
                "from typing import Union"
                if body_request_class and body_request_class.get("classes")
                else None
            ),

            replace_key_words_and_symbols(
                f'from {body_request_class.get("import")}'
                f'.{body_request_class.get("class").replace(".", "")}'
                f' import {body_request_class.get("class").replace(".", "")}'
            )
            if body_request_class and body_request_class.get("class") else "",

            replace_key_words_and_symbols(
                f'from {body_request_class.get("imports")}'
                f' import {body_request_class.get("classes").replace(".", "")}'
            )
            if body_request_class and body_request_class.get("classes")
            else "",

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
