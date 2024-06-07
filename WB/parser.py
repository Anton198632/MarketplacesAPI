import json
import os
import re
from pathlib import Path
from types import NoneType
from typing import Optional, Dict, Any, List, Union

import requests

from WB.constants import POST, GET, PUT, DELETE, PATCH
from WB.data_formaters import build_class_header, build_request_class

current_dir = Path(__file__).parent


class WBParser:

    def __init__(self, section):
        self.section = section

        self.section_dir = f"{current_dir}/{section}"
        self.schemas_dir = f"{self.section_dir}/schemas"
        os.makedirs(self.schemas_dir, exist_ok=True)
        self.request_bodies_dir = f"{self.section_dir}/requestBodies"
        os.makedirs(self.request_bodies_dir, exist_ok=True)
        self.responses_dir = f"{self.section_dir}/responses"
        os.makedirs(self.responses_dir, exist_ok=True)

    def create_class(self, class_name, properties, component, header=None):
        annotations = {}
        descriptions = {}
        imports = set()
        imports.add("from dataclasses import dataclass")

        import_pref = f"from WB.{self.section}.COMPONENT import "

        for name, value in properties.items():
            ref = value.get("$ref")
            if ref:
                cl = ref.split("/")
                cl_name = cl[len(cl) - 1]
                cl_name = f"{cl_name[0:1].upper()}{cl_name[1:]}"
                component_ = cl[len(cl) - 2]
                import_pref = import_pref.replace("COMPONENT", component_)

                field_annotation = type(cl_name, (), {})
                annotations[name] = field_annotation
                imports.add(f"{import_pref}{cl_name}")
                continue

            type_ = value.get("type")
            props = value.get("properties")
            if type_ == "object" and not props:
                field_annotation = Optional[Dict[str, Any]]
                imports.add("from typing import Optional")
                imports.add("from typing import Dict")
                imports.add("from typing import Any")

            elif type_ == "object" and props:
                name = f"{name[0].upper()}{name[1:]}"
                field_annotation = self.create_class(
                    f"{class_name}{name}", props, component
                )
                import_pref = import_pref.replace("COMPONENT", component)
                class_name = f"{class_name[0].upper()}{class_name[1:]}"
                imports.add(f"{import_pref}{class_name}{name}")

            elif type_ == "array":
                imports.add("from typing import List")
                items_type = value.get("items").get("type")
                ref = value.get("items").get("$ref")
                if ref:
                    cl = ref.split("/")
                    cl_name = cl[len(cl) - 1]
                    cl_name = f"{cl_name[0:1].upper()}{cl_name[1:]}"
                    component_ = cl[len(cl) - 2]
                    import_pref = import_pref.replace("COMPONENT", component_)

                    field_annotation = type(cl_name, (), {})
                    annotations[name] = field_annotation
                    imports.add(f"{import_pref}{cl_name}")
                    continue

                if items_type == "object":
                    props = value.get("items").get("properties")
                    name = f"{name[0].upper()}{name[1:]}"
                    field_annotation = List[
                        self.create_class(
                            class_name=f"{class_name}{name}",
                            properties=props,
                            component=component,
                        )
                    ]

                    import_pref = import_pref.replace("COMPONENT", component)

                    class_name = f"{class_name[0].upper()}{class_name[1:]}"
                    imports.add(
                        f"{import_pref}{class_name}{name}")

                elif items_type == "string":
                    field_annotation = List[str]
                elif items_type == "integer" or items_type == "number":
                    field_annotation = List[int]
                elif items_type == "boolean":
                    field_annotation = List[bool]
                else:
                    pass
                    field_annotation = List[Any]

            elif type_ == "boolean":
                field_annotation = bool
            elif type_ == "string":
                field_annotation = str
            elif type_ == "integer" or type_ == "number":
                field_annotation = int
            else:
                field_annotation = NoneType
                imports.add("from types import NoneType")

            annotations[f"{name[0].lower()}{name[1:]}"] = field_annotation
            descriptions[f"{name[0].lower()}{name[1:]}"] = (
                value.get("description") if value else None
            )

        # Создание класса с помощью функции type() с аннотациями
        class_name = f"{class_name[0:1].upper()}{class_name[1:]}"
        if "{" in class_name:
            cl_n_parts = re.split(r"[{}]", class_name)
            class_name = "".join(
                [f"{cl[0].upper()}{cl[1:]}" for cl in cl_n_parts]
            )
        class_ = type(class_name, (), annotations)

        self.write_class_to_script(
            class_, imports, annotations, component, descriptions, header
        )
        return class_

    def create(
        self,
        schema: str,
        value: dict,
        component: str,
        title: Optional[str] = None,
        description: Optional[str] = None
    ):
        type_ = value.get("type")
        import_pref = f"from WB.{self.section}.COMPONENT import "

        content = value.get("content")

        header = build_class_header(title, description)

        if content:
            app_json = content.get("application/json")
            if app_json:
                type_ = app_json.get("schema").get("type")
                value = app_json.get("schema")
                ref = app_json.get("schema").get("$ref")
                if ref:
                    cl = ref.split("/")
                    cl_name = cl[len(cl) - 1]
                    cl_name = f"{cl_name[0:1].upper()}{cl_name[1:]}"
                    component_ = cl[len(cl) - 2]
                    import_pref = import_pref.replace("COMPONENT", component_)
                    imports = set()
                    imports.add(f"{import_pref}{cl_name}")
                    self.write_const_to_scripts(
                        schema,
                        imports,
                        f"{schema}: {cl_name}\n",
                        component
                    )

        if type_ == "object":
            properties = value.get("properties")
            self.create_class(schema, properties, component, header)

        elif type_ == "array":
            items = value.get("items")
            items_type = value.get("items").get("type")
            if items.get("$ref"):
                cl = items.get("$ref").split("/")
                cl_name = cl[len(cl) - 1]
                cl_name = f"{cl_name[0:1].upper()}{cl_name[1:]}"
                component_ = cl[len(cl) - 2]
                import_pref = import_pref.replace("COMPONENT", component_)
                imports = set()
                imports.add("from typing import List")
                imports.add(f"{import_pref}{cl_name}")
                header = f'"""\n{title}\n{description}\n"""'
                self.write_const_to_scripts(
                    schema,
                    imports,
                    f"{schema}: List[{cl_name}] = []\n",
                    component
                )
            if items_type == "object":
                properties = value.get("items").get("properties")
                self.create_class(schema, properties, component, header)
            else:
                pass

        elif not type_:
            properties = value.get("properties")
            if properties:
                self.create_class(schema, properties, component, header)
            else:
                one_of = value.get("oneOf")
                if one_of:
                    schema = []
                    for i in range(0, len(one_of)):
                        ref = one_of[i].get("$ref")
                        if ref:
                            cl = ref.split("/")
                            cl_name = cl[len(cl) - 1]
                            schema.append(cl_name)
                        else:
                            pass
                else:
                    pass

        elif type_ == "string":
            self.write_const_to_scripts(
                schema, set(), f"{schema}: str\n", component
            )
            # return {"class": schema, "type": "str"}

        elif type_ == "integer":
            self.write_const_to_scripts(
                schema, set(), f"{schema}: int\n", component
            )
            # return {"class": schema, "type": "int"}
        else:
            pass

        return {"class": schema}

    def write_const_to_scripts(
            self, name: str, imports: set, data: str, component: str
    ):
        # Запись в файл-скрипт
        name = f"{name[0].upper()}{name[1:]}"
        filename = f"{self.section_dir}/{component}/{name}.py"
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

    def write_class_to_script(
            self,
            class_: type,
            imports: set,
            annotations: dict,
            component: str,
            descriptions: Optional[dict] = None,
            header: Optional[str] = None
    ):
        # Запись в файл-скрипт
        filename = f"{self.section_dir}/{component}/{class_.__name__}.py"
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

    # def replace_classes_in_files(self, replaces_classes):
    #     folder_path = Path(self.schemas_dir)
    #     classes_files = [f for f in folder_path.iterdir() if f.is_file()]
    #
    #     for classes_file in classes_files:
    #         with open(classes_file, "r", encoding='utf-8') as f:
    #             text = f.read()
    #         for replace_class in replaces_classes:
    #             new_type = replace_class.get("type")
    #             class_name = replace_class.get("class")
    #             if new_type:
    #                 text = text.replace(f"import {class_name}\n", "")
    #                 text = text.replace(f" {class_name}\n", f" {new_type}\n")
    #
    #         with open(classes_file, "w", encoding='utf-8') as f:
    #             f.write(text)

    def parse_paths(self):
        for key, value in self.paths.items():
            methods = [
                key for key in [POST, GET, PUT, DELETE, PATCH]
                if key in value
            ]

            for method in methods:
                content = value.get(method)

                title = content.get("summary")
                description = content.get("description")
                request_body = content.get("requestBody")
                responses = content.get("responses")

                if request_body:
                    class_name = "".join(
                        [
                            f"{k[0].upper()}{k[1:]}" if k != "" else ""
                            for k in key.strip().split("/")
                        ]
                    )
                    class_name_request = f"{class_name}Request"
                    body_request_class = self.create(
                        class_name_request,
                        request_body,
                        "requestBodies",
                        title,
                        description,
                    )
                else:
                    body_request_class = None

                responses_classes = {}
                if responses:
                    for status, response in responses.items():
                        class_name = "".join(
                            [
                                f"{k[0].upper()}{k[1:]}" if k != "" else ""
                                for k in key.strip().split("/")
                            ]
                        )
                        class_name_response = f"{class_name}Response{status}"
                        class_request = self.create(
                            class_name_response,
                            response,
                            "responses",
                            title,
                            description,
                        )

                        responses_classes[status] = class_name_response

                build_request_class(
                    section=self.section,
                    method=method,
                    url=key,
                    parameters=[],  # !!!!!!!!!!!
                    responses_classes=responses_classes,
                    body_request_class=body_request_class.get("class")
                )

                print(method, key, body_request_class, responses_classes)

                pass


    def parse_wb_api(self):
        response = requests.get(
            f"https://openapi.wildberries.ru/{self.section}/api/ru/"
        )
        text = response.text

        redoc_state = text[text.find("__redoc_state = ") + 16:]
        redoc_state = redoc_state[0: redoc_state.find(";\n")]

        api_json = json.loads(redoc_state)

        data = api_json.get("spec").get("data")

        with open(
            f"{self.section_dir}/wb_api_{self.section}.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        self.paths = data.get("paths")
        self.components = data.get("components")

        # получаем схемы
        schemas = self.components.get("schemas")
        for schema, value in schemas.items():
            self.create(schema, value, "schemas")

        # тела запросов
        request_bodies = self.components.get("requestBodies")
        if request_bodies:
            for request_body, value in request_bodies.items():
                self.create(
                    request_body, value, "requestBodies",
                )

        # ответы
        responses = self.components.get("responses")
        if responses:
            for response, value in responses.items():
                title = value.get("description").replace(" ", "")
                self.create(response, value, "responses", title)

        self.parse_paths()
