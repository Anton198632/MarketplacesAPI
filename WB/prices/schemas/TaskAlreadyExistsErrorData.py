from dataclasses import dataclass


@dataclass
class TaskAlreadyExistsErrorData:
    id: int
    alreadyExists: bool
