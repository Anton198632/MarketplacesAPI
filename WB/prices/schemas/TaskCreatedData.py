from dataclasses import dataclass


@dataclass
class TaskCreatedData:
    id: int
    alreadyExists: bool
