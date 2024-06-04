import inspect
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, List, get_type_hints, Union

import requests

current_dir = Path(__file__).parent


class WBParser:

    def __init__(self, section):
        self.section = section

        self.section_dir = f"{current_dir}/{section}"

        os.makedirs(self.section_dir, exist_ok=True)

    def create_class(self, class_name, properties) -> type:
        annotations = {}

        imports = set()
        imports.add('from dataclasses import dataclass')

        for field_name, field_info in properties.items():

            if field_name == "$ref":
                cl = field_info.split("/")
                field_annotation = cl[len(cl) - 1]
                imports.add(f"import {field_annotation}")
            else:
                field_type = field_info.get('type')
                props = field_info.get("properties")
                if field_type == "object" and not props:
                    field_annotation = Optional[Dict[str, Any]]
                    imports.add("from typing import Optional")
                    imports.add("from typing import Dict")
                    imports.add("from typing import Any")
                elif field_type == "object" and props:
                    sch = f"{class_name}_{field_name}"
                    field_annotation = self.create_class(sch, props)
                    imports.add(f"import {field_annotation.__name__}")
                elif field_type == "array":
                    props = field_info.get("items").get("properties")
                    sch = f"{class_name}_{field_name}"
                    field_annotation = List[self.create_class(sch, props)]
                    imports.add("from typing import List")
                    imports.add(f"import {field_annotation.__name__}")
                elif field_type == "boolean":
                    field_annotation = bool
                elif field_type == "string":
                    field_annotation = Optional[str]
                    imports.add("from typing import Optional")
                elif field_type == "integer":
                    field_annotation = Optional[int]
                    imports.add("from typing import Optional")
                else:
                    field_annotation = None
                    pass
            annotations[field_name] = field_annotation

        # Создание класса с помощью функции type() с аннотациями
        class_ = type(class_name, (), annotations)

        self.write_class_to_script(class_, imports, annotations)

        return class_

    def write_class_to_script(
            self, class_: type, imports: set, annotations: dict
    ):
        # Запись в файл-скрипт
        filename = f"{self.section_dir}/{class_.__name__}.py"
        with open(filename, 'w') as file:

            # Запись импортов
            for imp in imports:
                file.write(f"{imp}\n")
            file.write("\n\n")

            # Запись определения класса
            file.write(f"@dataclass\n")
            file.write(f"class {class_.__name__}:\n")

            for field_name, field_annotation in annotations.items():
                if hasattr(field_annotation, '__origin__'):
                    if field_annotation.__origin__ is Union and type(
                            None) in field_annotation.__args__:
                        non_none_args = [arg for arg in
                                         field_annotation.__args__ if
                                         arg is not type(None)]
                        annotation_str = f'Optional[{non_none_args[0].__name__}]'
                    else:
                        args = ', '.join(arg.__name__ for arg in
                                         field_annotation.__args__)
                        annotation_str = f'{field_annotation.__origin__.__name__}[{args}]'

                elif field_annotation:
                    annotation_str = field_annotation.__name__
                else:
                    annotation_str = None
                file.write(f"    {field_name}: {annotation_str}\n")

    def parse_wb_api(self):
        response = requests.get(
            f"https://openapi.wildberries.ru/{self.section}/api/ru/"
        )
        text = response.text

        redoc_state = text[text.find("__redoc_state = ") + 16:]
        redoc_state = redoc_state[0: redoc_state.find(";\n")]

        api_json = json.loads(redoc_state)

        data = api_json.get("spec").get("data")

        self.paths = data.get("paths")
        self.components = data.get("components")

        # получаем базовые схемы
        schemas = self.components.get("schemas")
        base_classes = []
        for schema, value in schemas.items():

            type_ = value.get("type")
            if type_ == "object":
                class_ = self.create_class(schema, value.get("properties"))
            elif type_ == "array":
                class_ = self.create_class(schema, value.get("items"))
            else:
                class_ = self.create_class(schema, value)
            base_classes.append(class_)


        pass
