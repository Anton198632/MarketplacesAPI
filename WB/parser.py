import json
import re
from pathlib import Path
from typing import Optional, Dict, Any, List

import requests

from WB.constants import POST, GET, PUT, DELETE, PATCH
from WB.data_formaters import (
    build_class_header, build_request_class, convert_type
)
from WB.file_helper import (
    build_path,
    write_class_to_script,
    write_descendant_class_to_script,
)

current_dir = Path(__file__).parent


def parse_ref(ref):
    cl = ref.split("/")
    cl_name = cl[len(cl) - 1]
    cl_name = f"{cl_name[0:1].upper()}{cl_name[1:]}"
    component_ = ref[2:ref.rfind("/")].replace("/", ".")
    return cl_name.replace(".", "").replace("-", "_"), component_


class WBParser:

    def __init__(self, section):
        self.parameters = []
        self.section = section

        self.section_dir = f'{current_dir}/{self.section.replace("-", "_")}'

    def create_class(
            self, class_name, properties, component, required, header=None,
    ):
        annotations = {}
        descriptions = {}
        imports = set()
        imports.add("from dataclasses import dataclass")

        class_name = class_name.replace(".", "")

        import_pref = f"from WB.{self.section}.COMPONENT.CLASS import "

        imports.add("from typing import Optional")

        if class_name == "Response200":
            pass

        for name, value in properties.items():
            ref = value.get("$ref")
            if ref:
                cl_name, component_ = parse_ref(ref)
                import_pref = (
                    import_pref.replace("COMPONENT", component_)
                )

                field_annotation = type(cl_name, (), {})
                annotations[name] = field_annotation
                imports.add(f'{import_pref}{cl_name.replace(".", "")}')
                continue

            type_ = value.get("type")
            format_ = value.get("format")
            props = value.get("properties")
            if type_ == "object" and not props:
                field_annotation = Dict[str, Any]
                imports.add("from typing import Dict")
                imports.add("from typing import Any")

            elif type_ == "object" and props:
                name_ = f"{name[0].upper()}{name[1:]}"
                field_annotation = self.create_class(
                    f"{class_name}{name_}", props, component, required
                )
                class_name = f"{class_name[0].upper()}{class_name[1:]}"
                import_pref = import_pref.replace(
                    "COMPONENT", component.replace("/", ".")
                )
                name_ = name_.replace(".", "")
                imports.add(f"{import_pref}{class_name}{name_}")

            elif type_ == "array":
                imports.add("from typing import List")
                items_type = value.get("items").get("type")
                ref = value.get("items").get("$ref")
                required_ = value.get("items").get("required")
                required_ = required_ if required_ else []
                if ref:
                    cl_name, component_ = parse_ref(ref)
                    import_pref = (
                        import_pref.replace("COMPONENT", component_)
                    )
                    field_annotation = type(cl_name, (), {})
                    annotations[name] = List[field_annotation]
                    imports.add(f"{import_pref}{cl_name}")
                    continue

                if items_type == "object":
                    props = value.get("items").get("properties")
                    name_ = f"{name[0].upper()}{name[1:]}"
                    if props:
                        field_annotation = List[
                            self.create_class(
                                class_name=f"{class_name}{name_}",
                                properties=props,
                                component=component,
                                required=required_
                            )
                        ]

                        class_name = f"{class_name[0].upper()}{class_name[1:]}"
                        import_pref = import_pref.replace(
                            "COMPONENT", component.replace("/", ".")
                        )

                        imports.add(f"{import_pref}{class_name}{name_}")
                    else:
                        field_annotation = Optional[List[Any]]
                        imports.add(f"from typing import Any")

                elif items_type == "string":
                    field_annotation = List[str]
                elif items_type == "integer" or items_type == "number":
                    field_annotation = List[int]
                elif items_type == "boolean":
                    field_annotation = List[bool]
                else:
                    field_annotation = List[Any]

            elif type_ == "boolean":
                field_annotation = bool

            elif type_ == "string":
                field_annotation = str
                if format_ == "binary":
                    field_annotation = bytes

            elif type_ == "integer" or type_ == "number":
                field_annotation = int

            else:
                field_annotation = Any
                imports.add("from typing import Any")

            if "vendorCode" in name:
                pass

            if (
                (isinstance(required, list) and name not in required)
                or (isinstance(required, bool) and required)
            ):
                field_annotation = Optional[field_annotation]
            else:
                pass

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
            header=header,
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
        import_pref = f"from WB.{self.section}.COMPONENT.CLASS import "

        content = value.get("content")

        header = build_class_header(title, description)

        required = value.get("required") if value.get("required") else []

        if content:
            for key, v in content.items():
                content_data = content.get(key)
                if key != "application/json":
                    pass

                type_ = content_data.get("schema").get("type")
                value = content_data.get("schema")
                ref = content_data.get("schema").get("$ref")
                if ref:
                    cl_name, component_ = parse_ref(ref)
                    import_pref = (
                        import_pref.replace("COMPONENT", component_)
                    )
                    imports = set()
                    imports.add("from dataclasses import dataclass")
                    imports.add(f"{import_pref}{cl_name}")
                    if "{" in schema:
                        cl_n_parts = re.split(r"[{}]", schema)
                        schema = "".join(
                            [
                                f"{cl[0].upper()}{cl[1:]}" if cl
                                else "" for cl
                                in cl_n_parts
                            ]
                        )
                    write_descendant_class_to_script(
                        path=f"WB/{self.section}/{component}",
                        name=schema,
                        imports=imports,
                        classes=[
                            {"class_name": schema, "base_class": cl_name},
                        ],
                    )

                else:
                    pass

        if type_ == "object":
            properties = value.get("properties")
            self.create_class(schema, properties, component, required, header)

        elif type_ == "array":
            items = value.get("items")
            items_type = value.get("items").get("type")
            required = items.get("required") if items.get("required") else []
            ref = items.get("$ref")
            if ref:
                cl_name, component_ = parse_ref(ref)
                import_pref = (
                    import_pref.replace("COMPONENT", component_)
                )
                imports = set()
                imports.add("from dataclasses import dataclass")
                imports.add("from typing import List")
                imports.add(f"{import_pref}{cl_name}")
                write_descendant_class_to_script(
                    path=f"WB/{self.section}/{component}",
                    name=schema,
                    imports=imports,
                    classes=[{"class_name": schema, "base_class": "list"}],
                )
            elif items_type == "object":
                properties = value.get("items").get("properties")
                self.create_class(
                    schema, properties, component, required, header
                )
            else:
                imports = set()
                imports.add("from dataclasses import dataclass")
                write_descendant_class_to_script(
                    path=f"WB/{self.section}/{component}",
                    name=schema,
                    imports=imports,
                    classes=[
                        {"class_name": schema, "base_class": "str"}
                    ],
                )

        elif not type_:
            properties = value.get("properties")
            if properties:
                self.create_class(
                    schema, properties, component, required, header
                )
            else:
                one_of = value.get("oneOf")
                ref = value.get("$ref")
                if one_of:
                    imports = set()
                    imports.add("from dataclasses import dataclass")
                    cls_names = []
                    for i in range(0, len(one_of)):
                        ref = one_of[i].get("$ref")
                        type_ = one_of[i].get("type")
                        if ref:
                            cl_name, component_ = parse_ref(ref)
                            import_pref_ = import_pref.replace(
                                "COMPONENT", component_
                            )
                            imports.add(f"{import_pref_}{cl_name}")
                            cls_names.append(cl_name)
                        elif type_ == "object":
                            cl_name = f"{schema}{i}"

                            properties = one_of[i].get("properties")
                            required = one_of[i].get("required")
                            self.create_class(
                                cl_name,
                                properties,
                                component,
                                required,
                                header
                            )
                            cls_names.append(cl_name)
                            import_pref_ = import_pref.replace(
                                "COMPONENT", component.replace("/", ".")
                            )
                            imports.add(f"{import_pref_}{cl_name}")
                        elif type_ == "string" or type_ == "integer":
                            type_ = convert_type(type_)
                            cl_name = f"{schema}{i}"
                            imports.add("from dataclasses import dataclass")
                            write_descendant_class_to_script(
                                path=f"WB/{self.section}/{component}",
                                name=cl_name,
                                imports=imports,
                                classes=[
                                    {
                                        "class_name": cl_name,
                                        "base_class": type_
                                    }
                                ],
                            )
                            import_pref_ = import_pref.replace(
                                "COMPONENT", component.replace("/", ".")
                            )
                            imports.add(f"{import_pref_}{cl_name}")
                            cls_names.append(cl_name)
                        else:
                            pass

                    classes = [
                        {
                            "class_name": f"{schema}{cl_name}",
                            "base_class": cl_name,
                        }
                        for cl_name in cls_names
                    ]
                    write_descendant_class_to_script(
                        path=f"WB/{self.section}/{component}",
                        name=schema,
                        imports=imports,
                        classes=classes
                    )

                    return {
                        "classes": (
                            ", ".join(
                                [
                                    class_.get("class_name")
                                    for class_ in classes
                                ]
                            )
                        ),
                        "module": schema
                    }

                elif ref:
                    cl_name, component_ = parse_ref(ref)
                    import_pref = (
                        import_pref.replace("COMPONENT", component_)
                    )

                    imports = set()
                    imports.add("from dataclasses import dataclass")
                    imports.add(f"{import_pref}{cl_name}")
                    write_descendant_class_to_script(
                        path=f"WB/{self.section}/{component}",
                        name=schema,
                        imports=imports,
                        classes=[
                            {"class_name": schema, "base_class": cl_name}
                        ],
                    )
                else:
                    imports = set()
                    imports.add("from dataclasses import dataclass")
                    write_descendant_class_to_script(
                        path=f"WB/{self.section}/{component}",
                        name=schema,
                        imports=imports,
                        classes=[
                            {"class_name": schema, "base_class": "str"}
                        ],
                    )

        elif type_ == "string" or type_ == "integer":
            type_ = convert_type(type_)
            imports = set()
            imports.add("from dataclasses import dataclass")
            write_descendant_class_to_script(
                path=f"WB/{self.section}/{component}",
                name=schema,
                imports=imports,
                classes=[{"class_name": schema, "base_class": type_}]
            )

        else:
            pass

        return f"{schema[0].upper()}{schema[1:]}"

    def parse_paths(self, paths):
        for key, value in paths.items():
            methods = [
                key for key in [POST, GET, PUT, DELETE, PATCH]
                if key in value
            ]

            for method in methods:
                content = value.get(method)

                title = content.get("summary")
                description = content.get("description")
                request_body = content.get("requestBody")

                if request_body:

                    component_path = (
                        f"requestBodies{key}/{method}"
                    )
                    build_path(f"WB/{self.section}/{component_path}")
                    class_name_request = f"RequestBody"
                    class_ = self.create(
                        schema=class_name_request,
                        value=request_body,
                        component=component_path,
                    )
                    if isinstance(class_, str):
                        body_request_class = {
                            "class": class_,
                            "import": (
                                f"WB/{self.section}/{component_path}"
                                .replace("/", ".")
                            ),
                        }
                    else:
                        body_request_class = {
                            "classes": class_.get("classes"),
                            "imports": (
                                f"WB/{self.section}/{component_path}"
                                f'/{class_.get("module")}'
                                .replace("/", ".")
                            ),
                        }
                    pass
                else:
                    body_request_class = None

                parameters = content.get("parameters")
                parameters_data = []
                if parameters:
                    for parameter in parameters:
                        ref = parameter.get("$ref")
                        if ref:
                            name = ref.split("/")[-1]
                            parameter_data = list(
                                filter(
                                    lambda p: p.get("name") == name,
                                    self.parameters,
                                )
                            )[0]
                            parameters_data.append(parameter_data)
                        else:
                            original_name = parameter.get("name")
                            if "[" in original_name:
                                original_name = original_name[
                                    0: original_name.find("[")
                                ]
                            parameters_data.append(
                                {
                                    "name": parameter.get("name"),
                                    "original_name": original_name,
                                    "in": parameter.get("in"),
                                    "description": (
                                        parameter.get("description")
                                    ),
                                    "required": (
                                        True if parameter.get("required")
                                        else False
                                    ),
                                    "type": convert_type(
                                        parameter.get("schema").get("type")
                                    ),
                                }
                            )
                            pass

                    parameters_data.sort(key=lambda p: p.get("required"))
                    parameters_data.reverse()

                responses = content.get("responses")
                responses_classes = {}
                if responses:
                    for status, response in responses.items():
                        component_path = (
                            f"responses{key}/{method}"
                        )
                        build_path(f"WB/{self.section}/{component_path}")
                        class_name_response = f"Response{status}"
                        class_response = self.create(
                            schema=class_name_response,
                            value=response,
                            component=component_path,
                        )

                        if isinstance(class_response, str):
                            responses_classes[status] = {
                                "class": class_response,
                                "import": (
                                    f"WB/{self.section}/{component_path}"
                                    f"/{class_response}"
                                    .replace("/", ".")
                                ),
                                "status_code": status,
                            }
                        else:
                            responses_classes[status] = {
                                "classes": class_response.get("classes"),
                                "imports": (
                                    f"WB/{self.section}/{component_path}"
                                    f'/{class_response.get("module")}'
                                    .replace("/", ".")
                                ),
                                "status_code": status,
                            }
                        pass

                build_request_class(
                    section=self.section,
                    method=method,
                    url=key,
                    parameters=parameters_data,
                    responses_classes=responses_classes,
                    body_request_class=body_request_class,
                    description=build_class_header(title, description)
                )

    def parse_wb_api(self):
        response = requests.get(
            f"https://openapi.wildberries.ru/{self.section}/api/ru/"
        )
        self.section = self.section.replace("-", "_")

        text = response.text

        redoc_state = text[text.find("__redoc_state = ") + 16:]
        redoc_state = redoc_state[0: redoc_state.find(";\n")]

        api_json = json.loads(redoc_state)

        data = api_json.get("spec").get("data")

        build_path(self.section_dir)

        with open(
            f"{self.section_dir}/wb_api_{self.section}.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        components = data.get("components")

        # получаем схемы
        schemas = components.get("schemas")
        if schemas:
            build_path(f"WB/{self.section}/components/schemas")
            for schema, value in schemas.items():
                self.create(schema, value, "components/schemas")

        # тела запросов
        request_bodies = components.get("requestBodies")
        if request_bodies:
            build_path(f"WB/{self.section}/components/requestBodies")
            for request_body, value in request_bodies.items():
                self.create(
                    request_body, value, "components/requestBodies",
                )

        # Параметрв запросов
        parameters = components.get("parameters")
        if parameters:
            for parameter, value in parameters.items():
                type_ = value.get("schema").get("type")
                type_ = convert_type(type_)

                self.parameters.append(
                    {
                        "name": parameter,
                        "original_name": value.get("name"),
                        "in": value.get("in"),
                        "description": value.get("description"),
                        "required": True if value.get("required") else False,
                        "type": type_
                    }
                )

        # ответы
        responses = components.get("responses")
        build_path(f"WB/{self.section}/components/responses")
        if responses:
            for response, value in responses.items():
                title = value.get("description").replace(" ", "")
                self.create(response, value, "components/responses", title)

        # маршруты
        paths = data.get("paths")
        self.parse_paths(paths)
