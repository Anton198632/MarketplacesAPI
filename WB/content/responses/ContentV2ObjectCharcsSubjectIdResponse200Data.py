from dataclasses import dataclass


@dataclass
class ContentV2ObjectCharcsSubjectIdResponse200Data:
    #  Идентификатор характеристики
    charcID: int
    #  Название предмета
    subjectName: str
    #  Идентификатор предмета
    subjectID: int
    #  Название характеристики
    name: str
    #  true - характеристику необходимо обязательно указать в КТ. false - харак
    #  теристику не обязательно указывать
    required: bool
    #  Единица измерения
    unitName: str
    #  Максимальное кол-во значений, которое можно присвоить данной характерист
    #  ике. Если 0, то нет ограничения.
    maxCount: int
    #  Характеристика популярна у пользователей (true - да, false - нет)
    popular: bool
    #  Тип характеристики (1 и 0 - строка или массив строк; 4 - число или масси
    #  в чисел)
    charcType: int
