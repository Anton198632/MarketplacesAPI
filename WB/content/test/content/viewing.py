from WB.content.requests.viewing.cards_list_data import (
    Cursor,
    CardsListData,
    Settings,
    Sort,
    Filter,
)
from WB.content.requests.viewing.request_get_cards_list import (
    RequestGetCardsListAPI,
)
from WB.content.responses.viewing.response_cards_list import ResponseCardList
from WB.content.test.constants import WB_API_KEY


def get_card_list():
    cards = []
    cursor = Cursor(limit=10)
    while True:

        data: ResponseCardList = RequestGetCardsListAPI(WB_API_KEY).execute(
            card_list_data=CardsListData(
                settings=Settings(
                    sort=Sort(ascending=True),
                    filter=Filter(withPhoto=-1),
                    cursor=cursor
                )
            )
        )

        cards += data.cards
        cursor = data.cursor

        if len(data.cards) < 10:
            break

    return cards
