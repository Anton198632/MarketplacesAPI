import json

import requests


def get_body_by_ref(ref: str, data):
    keys = ref.strip("#/").split("/")
    value = data
    try:
        for key in keys:
            value = value[key]
    except KeyError:
        pass

    required = value.get("required")

    properties = value.get("contenet")


    pass



def parse_wb_api(section: str):
    response = requests.get(
        f"https://openapi.wildberries.ru/{section}/api/ru/"
    )
    text = response.text

    redoc_state = text[text.find("__redoc_state = ") + 16:]
    redoc_state = redoc_state[0: redoc_state.find(";\n")]

    api_json = json.loads(redoc_state)

    data = api_json.get("spec").get("data")

    paths = data.get("paths")


    apis_data = []
    for key, value in paths.items():
        methods = [
            key for key in ["post", "get", "put", "delete", "patch"]
            if key in value
        ]

        for method in methods:
            content = value.get(method)

            title = content.get("summary")
            description = content.get("description")
            request_body = content.get("requestBody")

            ref = request_body.get("$ref")
            if ref:
                get_body_by_ref(ref, data)

            pass


def get_wb_api(section: str) -> dict:
    response = requests.get(
        f"https://openapi.wildberries.ru/{section}/api/ru/"
    )
    text = response.text

    redoc_state = text[text.find("__redoc_state = ") + 16:]
    redoc_state = redoc_state[0: redoc_state.find(";\n")]

    api_json = json.loads(redoc_state)

    return api_json.get("spec").get("data")

    # paths = api_json.get("spec").get("data").get("paths")
    #
    # components = (
    #     api_json.get("spec").get("data").get("components").get("schemas")
    # )
    #
    # apis_data = []
    # for key, value in paths.items():
    #     methods = [
    #         key for key in ["post", "get", "put", "delete", "patch"]
    #         if key in value
    #     ]
    #
    #     for method in methods:
    #         content = value.get(method)
    #
    #         title = content.get("summary")
    #         description = content.get("description")
    #         request_body = content.get("requestBody")
    #
    #         body = None
    #         if request_body:
    #             content_body = request_body.get("content")
    #             for k, v in content_body.items():
    #                 schema = v.get("schema")
    #
    #                 if schema.get("oneOf"):
    #                     data = []
    #                     for variant in schema.get("oneOf"):
    #                         r = variant.get("$ref")
    #                         ref = r[r.rfind("/") + 1:]
    #                         # data.append(
    #                         #     json.dumps(
    #                         #         components.get(ref), ensure_ascii=False
    #                         #     )
    #                         # )
    #                         data.append(components.get(ref))
    #                 else:
    #                     # data = [json.dumps(schema, ensure_ascii=False)]
    #                     data = [schema]
    #                 body = Body(type=k, data=data)
    #
    #         response = content.get("responses")
    #         # response = (
    #         #     json.dumps(response, ensure_ascii=False) if response else None
    #         # )
    #
    #         apis_data.append(
    #             ItemAPI(
    #                 server=value.get("servers")[0].get("url"),
    #                 url=key,
    #                 method=method,
    #                 title=title,
    #                 description=description,
    #                 body=body,
    #                 parameters=content.get("parameters"),
    #                 responses=response
    #             )
    #         )
    # return API(responses=apis_data)
