import json
import os
import re
from pathlib import Path
from types import NoneType
from typing import Optional, Dict, Any, List, Union

import requests

from WB.constants import POST, GET, PUT, DELETE, PATCH
from WB.data_formaters import build_class_header, build_request_class
from WB.file_helper import (
    build_path,
    write_class_to_script,
    write_const_to_scripts,
)

current_dir = Path(__file__).parent


class WBParser:

    def __init__(self, section):
        self.section = section

        self.section_dir = f"{current_dir}/{section}"
        # self.request_bodies_dir = f"{self.section_dir}/requestBodies"
        # os.makedirs(self.request_bodies_dir, exist_ok=True)
        # self.responses_dir = f"{self.section_dir}/responses"
        # os.makedirs(self.responses_dir, exist_ok=True)

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
                import_pref = import_pref.replace(
                    "COMPONENT", component.replace("/", ".")
                )
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

                    import_pref = import_pref.replace(
                        "COMPONENT", component.replace("/", ".")
                    )

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
                [f"{cl[0].upper()}{cl[1:]}" if cl else "" for cl in cl_n_parts]
            )
        class_ = type(class_name, (), annotations)

        write_class_to_script(
            path=f"WB/{self.section}/{component}",
            class_=class_,
            imports=imports,
            annotations=annotations,
            descriptions=descriptions,
            header=header
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
                    component_ = ref[2:ref.rfind("/")].replace("/", ".")
                    import_pref = import_pref.replace("COMPONENT", component_)
                    imports = set()
                    imports.add(f"{import_pref}{cl_name}")
                    if "{" in schema:
                        !!!!!!!
                        pass
                    write_const_to_scripts(
                        path=f"WB/{self.section}/{component}",
                        name=schema,
                        imports=imports,
                        data=f"{schema}: {cl_name}\n",
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
                write_const_to_scripts(
                    path=f"WB/{self.section}/{component}",
                    name=schema,
                    imports=imports,
                    data=f"{schema}: List[{cl_name}] = []\n",
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
            write_const_to_scripts(
                path=f"WB/{self.section}/{component}",
                name=schema,
                imports=set(),
                data=f"{schema}: str\n",
            )

        elif type_ == "integer":
            write_const_to_scripts(
                path=f"WB/{self.section}/{component}",
                name=schema,
                imports=set(),
                data=f"{schema}: int\n",
            )

        else:
            pass

        return {"class": schema}

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

                    component_path = f"requestBodies{key[0:key.rfind('/')]}"
                    build_path(f"WB/{self.section}/{component_path}")
                    # class_name = "".join(
                    #     [
                    #         f"{k[0].upper()}{k[1:]}" if k != "" else ""
                    #         for k in key.strip().split("/")
                    #     ]
                    # )
                    class_name = key[key.rfind("/") + 1:]
                    class_name_request = f"{class_name}Request"
                    body_request_class = self.create(
                        schema=class_name_request,
                        value=request_body,
                        component=component_path,
                        title=title,
                        description=description,
                    )
                else:
                    body_request_class = None

                responses_classes = {}
                if responses:
                    for status, response in responses.items():
                        # class_name = "".join(
                        #     [
                        #         f"{k[0].upper()}{k[1:]}" if k != "" else ""
                        #         for k in key.strip().split("/")
                        #     ]
                        # )
                        component_path = f"responses{key[0:key.rfind('/')]}"
                        build_path(f"WB/{self.section}/{component_path}")
                        class_name = key[key.rfind("/") + 1:]
                        class_name_response = f"{class_name}Response{status}"
                        class_request = self.create(
                            schema=class_name_response,
                            value=response,
                            component=component_path,
                            title=title,
                            description=description,
                        )

                        responses_classes[status] = class_name_response

                # build_request_class(
                #     section=self.section,
                #     method=method,
                #     url=key,
                #     parameters=[],  # !!!!!!!!!!!
                #     responses_classes=responses_classes,
                #     body_request_class=body_request_class.get("class")
                # )
                #
                # print(method, key, body_request_class, responses_classes)

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
        build_path(f"WB/{self.section}/components/schemas")
        for schema, value in schemas.items():
            self.create(schema, value, "components/schemas")

        # тела запросов
        request_bodies = self.components.get("requestBodies")
        build_path(f"WB/{self.section}/components/requestBodies")
        if request_bodies:
            for request_body, value in request_bodies.items():
                self.create(
                    request_body, value, "components/requestBodies",
                )

        # ответы
        responses = self.components.get("responses")
        build_path(f"WB/{self.section}/components/responses")
        if responses:
            for response, value in responses.items():
                title = value.get("description").replace(" ", "")
                self.create(response, value, "components/responses", title)

        self.parse_paths()
