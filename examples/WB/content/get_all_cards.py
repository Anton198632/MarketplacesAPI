import os

from dotenv import load_dotenv

from WB.content.ContentV2GetCardsListPost import ContentV2GetCardsListPost
from WB.content.requestBodies.content.v2.get.cards.list.post. \
    RequestBody import RequestBody
from WB.content.requestBodies.content.v2.get.cards.list.post. \
    RequestBodySettings import RequestBodySettings
from WB.content.requestBodies.content.v2.get.cards.list.post. \
    RequestBodySettingsCursor import RequestBodySettingsCursor
from WB.content.requestBodies.content.v2.get.cards.list.post. \
    RequestBodySettingsFilter import RequestBodySettingsFilter
from WB.content.requestBodies.content.v2.get.cards.list.post. \
    RequestBodySettingsSort import RequestBodySettingsSort
from WB.content.responses.content.v2.get.cards.list.post.Response200 import (
    Response200,
)
from WB.content.responses.content.v2.get.cards.list.post. \
    Response200Cursor import Response200Cursor
from WB.utils import create_combined_dataclass
from create_logger import create_logger

logger = create_logger(__name__)

CombinedCursor = create_combined_dataclass(
    'CombinedCursor', RequestBodySettingsCursor, Response200Cursor
)


def get_all_cards():
    load_dotenv()
    api_key = os.getenv('WB_API_KEY')

    cursor = RequestBodySettingsCursor(limit=100)

    cards = []

    request = ContentV2GetCardsListPost(api_key)

    while True:
        response = request.execute(
            body_request=RequestBody(
                settings=RequestBodySettings(
                    sort=RequestBodySettingsSort(True),
                    filter=RequestBodySettingsFilter(withPhoto=-1, ),
                    cursor=cursor
                ),
            ),
        )

        if not isinstance(response, Response200):
            logger.warning(response)
            break

        total = response.cursor.total
        cards += response.cards

        logger.info(f"{total} entries received. Total - {len(cards)}")

        if total < 100:
            break

        cursor = CombinedCursor(
            limit=cursor.limit,
            updatedAt=response.cursor.updatedAt,
            nmID=response.cursor.nmID,
        )

    return cards
