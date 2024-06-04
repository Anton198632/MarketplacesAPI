import json
from typing import Dict


def dict_write(filename: str, data: Dict) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
