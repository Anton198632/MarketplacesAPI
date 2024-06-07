from dataclasses import dataclass


@dataclass
class ContentV2DirectoryTnvedResponse200Data:
    #  ТНВЭД-код
    tnved: str
    #  - `true` - код маркировки требуется
    #  - `false` - код маркировки не требуе
    #  тся
    isKiz: bool
