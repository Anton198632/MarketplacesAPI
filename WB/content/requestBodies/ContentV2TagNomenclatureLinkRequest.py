from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2TagNomenclatureLinkRequest:
    """
    Управление тегами в КТ
    Метод позволяет добавить теги к КТ и снять их с КТ.<br> При снятии тега с К
    Т сам тег не удаляется.<br> К карточке можно добавить 15 тегов.
    """
    #  Артикул WB
    nmID: int
    #  Массив числовых идентификаторов тегов.   Что бы снять теги с КТ, необход
    #  имо передать пустой массив. Чтобы добавить теги к уже имеющимся в КТ, не
    #  обходимо в запросе передать новые теги и теги, которые уже есть в КТ.
    tagsIDs: List[int]
