import json
import os
from pathlib import Path
from types import NoneType
from typing import Optional, Dict, Any, List, Union

import requests

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

    def create_class(self, class_name, properties, component):
        annotations = {}
        imports = set()
        imports.add("from dataclasses import dataclass")

        import_pref = f"from WB.{self.section}.COMPONENT import "

        for name, value in properties.items():
            ref = value.get("$ref")
            if ref:
                cl = ref.split("/")
                cl_name = cl[len(cl) - 1]
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
                field_annotation = self.create_class(
                    f"{class_name}{name.capitalize()}", props, component
                )
                import_pref = import_pref.replace("COMPONENT", component)
                imports.add(f"{import_pref}{class_name}{name.capitalize()}")

            elif type_ == "array":
                imports.add("from typing import List")
                items_type = value.get("items").get("type")
                ref = value.get("items").get("$ref")
                if ref:
                    cl = ref.split("/")
                    cl_name = cl[len(cl) - 1]
                    component_ = cl[len(cl) - 2]
                    import_pref = import_pref.replace("COMPONENT", component_)

                    field_annotation = type(cl_name, (), {})
                    annotations[name] = field_annotation
                    imports.add(f"{import_pref}{cl_name}")
                    continue

                if items_type == "object":
                    props = value.get("items").get("properties")
                    field_annotation = List[
                        self.create_class(
                            f"{class_name}{name.capitalize()}", props,
                            component
                        )
                    ]

                    import_pref = import_pref.replace("COMPONENT", component)
                    imports.add(
                        f"{import_pref}{class_name}{name.capitalize()}")

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

            annotations[name] = field_annotation

        # Создание класса с помощью функции type() с аннотациями
        class_ = type(class_name, (), annotations)

        self.write_class_to_script(class_, imports, annotations, component)
        return class_

    def create(self, schema, value, component):
        type_ = value.get("type")
        import_pref = f"from WB.{self.section}.COMPONENT import "

        content = value.get("content")

        if content:
            app_json = content.get("application/json")
            if app_json:
                type_ = app_json.get("schema").get("type")
                value = app_json.get("schema")
                ref = app_json.get("schema").get("$ref")
                if ref:
                    cl = ref.split("/")
                    cl_name = cl[len(cl) - 1]
                    component_ = cl[len(cl) - 2]
                    import_pref = import_pref.replace("COMPONENT", component_)
                    imports = set()
                    imports.add(f"{import_pref}{cl_name}")
                    self.write_const_to_scripts(
                        schema, imports, f"{schema}: {cl_name}\n", component
                    )

        if type_ == "object":
            properties = value.get("properties")
            self.create_class(schema, properties, component)

        elif type_ == "array":
            items = value.get("items")
            items_type = value.get("items").get("type")
            if items.get("$ref"):
                cl = items.get("$ref").split("/")
                cl_name = cl[len(cl) - 1]
                component_ = cl[len(cl) - 2]
                import_pref = import_pref.replace("COMPONENT", component_)
                imports = set()
                imports.add("from typing import List")
                imports.add(f"{import_pref}{cl_name}")

                self.write_const_to_scripts(
                    schema,
                    imports, f"{schema}: List[{cl_name}] = []\n",
                    component
                )
            if items_type == "object":
                properties = value.get("items").get("properties")
                self.create_class(schema, properties, component)
            else:
                pass

        elif not type_:
            properties = value.get("properties")
            if properties:
                self.create_class(schema, properties, component)
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
        filename = f"{self.section_dir}/{component}/{name}.py"
        with open(filename, 'w') as file:
            # Запись импортов
            for imp in imports:
                file.write(f"{imp}\n")
            file.write("\n\n")

            file.write(data)

    def write_class_to_script(
            self, class_: type, imports: set, annotations: dict, component: str
    ):
        # Запись в файл-скрипт
        filename = f"{self.section_dir}/{component}/{class_.__name__}.py"
        with open(filename, 'w') as file:

            # Запись импортов
            for imp in imports:
                file.write(f"{imp}\n")
            file.write("\n\n")

            # Запись определения класса
            file.write(f"@dataclass\n")
            file.write(f"class {class_.__name__}:\n")

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
                file.write(f"    {field_name}: {annotation_str}\n")

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
                key for key in ["post", "get", "put", "delete", "patch"]
                if key in value
            ]

            for method in methods:
                content = value.get(method)

                title = content.get("summary")
                description = content.get("description")
                request_body = content.get("requestBody")

                if request_body:
                    class_name = "".join(
                        [k.capitalize() for k in key.split("/")]
                    )
                    class_name = f"{class_name}Request"
                    class_ = self.create(
                        class_name, request_body, "requestBodies"
                    )
                else:
                    class_ = None

                print(method, key, class_)

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
                self.create(request_body, value, "requestBodies")

        # ответы
        responses = self.components.get("responses")
        if responses:
            for response, value in responses.items():
                self.create(response, value, "responses")

        self.parse_paths()
