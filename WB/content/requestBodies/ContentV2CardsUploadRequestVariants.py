from WB.content.requestBodies import ContentV2CardsUploadRequestVariantsSizes
from typing import List
from WB.content.requestBodies import (
    ContentV2CardsUploadRequestVariantsCharacteristics,
)
from dataclasses import dataclass
from WB.content.requestBodies import (
    ContentV2CardsUploadRequestVariantsDimensions,
)


@dataclass
class ContentV2CardsUploadRequestVariants:
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
    #  Артикул продавца
    vendorCode: str
    #  Габариты упаковки товара. Указывать в **сантиметрах** для любого товара.
    #   
    #   
    #  Если не указать структуру dimensions в запросе, то она сгенерируется
    #   системой автоматически с нулевыми значениями длины, ширины, высоты
    dimensions: ContentV2CardsUploadRequestVariantsDimensions
    #  Массив с размерами.  
    #  Если для размерного товара (обувь, одежда и др.) н
    #  е указать этот массив, то системой в карточке он будет сгенерирован авто
    #  матически с `techSize` = "A" и `wbSize` = "1" и баркодом.
    sizes: List[ContentV2CardsUploadRequestVariantsSizes]
    #  Массив характеристик товара
    characteristics: List[ContentV2CardsUploadRequestVariantsCharacteristics]
