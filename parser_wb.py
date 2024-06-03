import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Union

import requests


@dataclass
class Body:
    type: str
    data: List[Dict]


@dataclass
class ItemAPI:
    server: str
    url: str
    method: str
    title: str
    description: str
    body: Optional[Body]
    parameters: Optional[List]
    responses: Union[Dict, str, None]


if __name__ == "__main__":
    response = requests.get("https://openapi.wildberries.ru/content/api/ru/")
    text = response.text

    redoc_state = text[text.find("__redoc_state = ") + 16 :]
    redoc_state = redoc_state[0 : redoc_state.find(";\n")]

    api_json = json.loads(redoc_state)

    paths = api_json.get("spec").get("data").get("paths")

    components = (
        api_json.get("spec").get("data").get("components").get("schemas")
    )

    apis_data = []
    for key, value in paths.items():
        method = next(
            (
                key for key in ["post", "get", "put", "delete", "path"]
                if key in value
            ),
            None
        )

        content = value.get(method)

        title = content.get("summary")
        description = content.get("description")
        request_body = content.get("requestBody")

        body = None
        if request_body:
            content_body = request_body.get("content")
            for k, v in content_body.items():
                schema = v.get("schema")
                data = [schema]
                if schema.get("oneOf"):
                    data = []
                    for variant in schema.get("oneOf"):
                        r = variant.get("$ref")
                        ref = r[r.rfind("/") + 1 :]
                        data.append(components.get(ref))

                body = Body(type=k, data=data)

        apis_data.append(
            ItemAPI(
                server=value.get("servers")[0].get("url"),
                url=key,
                method=method,
                title=title,
                description=description,
                body=body,
                parameters=content.get("parameters"),
                responses=content.get("responses")
            )
        )

    pass
