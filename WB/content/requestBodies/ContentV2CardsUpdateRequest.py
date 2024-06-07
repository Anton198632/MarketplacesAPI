from WB.content.requestBodies import ContentV2CardsUpdateRequestDimensions
from WB.content.requestBodies import ContentV2CardsUpdateRequestSizes
from WB.content.requestBodies import ContentV2CardsUpdateRequestCharacteristics
from typing import List
from dataclasses import dataclass


@dataclass
class ContentV2CardsUpdateRequest:
    """
    Редактирование КТ

    Обновляет карточку товара. Данные для обновления можно получить с помощью метода [Список номенклатур (НМ)](./#tag/Prosmotr/paths/~1content~1v2~1get~1cards~1list/post)
    
    Нельзя редактировать или удалить баркоды, но можно добавить баркод к существующему. Параметры `photos`, `video` и `tags` передавать не обязательно, их нельзя редактировать или удалять в этом методе.
    
    Если ответ Успешно (200), но какие-то карточки не изменились, проверьте ошибки с помощью метода `Список несозданных номенклатур (НМ) с ошибками`.
    
    В одном запросе можно отредактировать максимум 3000 номенклатур (`nmID`). Максимальный размер запроса 10 Мб.
    
    Габариты товаров можно указать только в **сантиметрах**.
    
    """
    #  Артикул WB
    nmID: int
    #  Артикул продавца
    vendorCode: str
    #  Бренд
    brand: str
    #  Наименование товара
    title: str
    #  Описание товара. Максимальное количество символов зависит от категории т
    #  овара. Стандарт — 2000, минимум — 1000, максимум — 5000.
    #  Подробно о прав
    #  илах описания в **Правилах заполнения карточки товара** в разделе [Инстр
    #  укции](https://seller.wildberries.ru/training) на портале продавцов.
    description: str
    #  Габариты упаковки товара. Указывать в **сантиметрах** для любого товара.
    Dimensions: ContentV2CardsUpdateRequestDimensions
    #  Характеристики товара
    Characteristics: List[ContentV2CardsUpdateRequestCharacteristics]
    #  Массив размеров артикула.  Для безразмерного товара все равно нужно пере
    #  давать данный массив без параметров (wbSize и techSize), но с баркодом.
    Sizes: List[ContentV2CardsUpdateRequestSizes]
