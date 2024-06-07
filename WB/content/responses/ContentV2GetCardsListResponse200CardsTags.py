from dataclasses import dataclass


@dataclass
class ContentV2GetCardsListResponse200CardsTags:
    #  Идентификатор тега
    id: int
    #  Название тега
    name: str
    #  Цвет тега. <dl> <dt>Доступные цвета:</dt> <dd><code>D1CFD7</code> - серы
    #  й</dd> <dd><code>FEE0E0</code> - красный</dd> <dd><code>ECDAFF</code> - 
    #  фиолетовый</dd> <dd><code>E4EAFF</code> - синий</dd> <dd><code>DEF1DD</c
    #  ode> - зеленый</dd> <dd><code>FFECC7</code> - желтый</dd> </dl>
    color: str