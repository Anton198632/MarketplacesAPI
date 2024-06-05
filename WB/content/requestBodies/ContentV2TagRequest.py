from dataclasses import dataclass


@dataclass
class ContentV2TagRequest:
    color: str
    name: str
