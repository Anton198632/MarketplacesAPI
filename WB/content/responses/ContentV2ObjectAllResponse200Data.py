from dataclasses import dataclass


@dataclass
class ContentV2ObjectAllResponse200Data:
    #  Идентификатор предмета
    subjectID: int
    #  Идентификатор родительской категории
    parentID: int
    #  Название предмета
    subjectName: str
    #  Название родительской категории
    parentName: str
