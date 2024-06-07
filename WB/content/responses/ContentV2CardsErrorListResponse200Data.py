from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2CardsErrorListResponse200Data:
    #  Категория для который создавалось КТ с данной НМ
    object: str
    #  Артикул продавца
    vendorCode: str
    #  Дата и время запроса на создание КТ с данным НМ
    updateAt: str
    #  Список ошибок из-за которых не обработался запрос на создание КТ с данны
    #  м НМ
    errors: List[str]
    #  Идентификатор предмета
    objectID: int
