from WB.content.requestBodies import (
    ContentV2CardsUploadAddRequestCardsToAddCharacteristics,
)
from WB.content.requestBodies import (
    ContentV2CardsUploadAddRequestCardsToAddDimensions,
)
from dataclasses import dataclass
from WB.content.requestBodies import (
    ContentV2CardsUploadAddRequestCardsToAddSizes,
)
from typing import List


@dataclass
class ContentV2CardsUploadAddRequestCardsToAdd:
    #  Бренд
    brand: str
    #  Артикул продавца
    vendorCode: str
    #  Наименование товара
    title: str
    #  Описание товара. Максимальное количество символов зависит от категории т
    #  овара. Стандарт — 2000, минимум — 1000, максимум — 5000.
    #  Подробно о прав
    #  илах описания в **Правилах заполнения карточки товара** в разделе [Инстр
    #  укции](https://seller.wildberries.ru/training) на портале продавцов.
    description: str
    #  Габариты упаковки товара. Указывать в **сантиметрах** для любого товара.
    #   
    #   
    #  Если не указать структуру dimensions в запросе, то она сгенерируется
    #   системой автоматически с нулевыми значениями длины, ширины, высоты
    dimensions: ContentV2CardsUploadAddRequestCardsToAddDimensions
    #  Характеристики товара
    characteristics: List[ContentV2CardsUploadAddRequestCardsToAddCharacteristics]
    #  Массив с размерами.  
    #  Если для размерного товара (обувь, одежда и др.) н
    #  е указать этот массив, то системой в карточке он будет сгенерирован авто
    #  матически с `techSize` = "A" и `wbSize` = "1" и баркодом.
    sizes: List[ContentV2CardsUploadAddRequestCardsToAddSizes]
