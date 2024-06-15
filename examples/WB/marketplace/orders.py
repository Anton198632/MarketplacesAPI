import datetime
import os
from typing import List

from dotenv import load_dotenv

from WB.marketplace.ApiV3OrdersGet import ApiV3OrdersGet
from WB.marketplace.ApiV3OrdersNewGet import ApiV3OrdersNewGet
from WB.marketplace.ApiV3OrdersStatusPost import ApiV3OrdersStatusPost
from WB.marketplace.ApiV3OrdersStickersPost import ApiV3OrdersStickersPost
from WB.marketplace.responses.api.v3.orders.get.Response200 import Response200
from WB.marketplace.responses.api.v3.orders.new.get.Response200 import (
    Response200 as NewOrdersResponse200,
)
from WB.marketplace.requestBodies.api.v3.orders.status.post.\
    RequestBody import RequestBody as OrdersForGetStatus
from WB.marketplace.responses.api.v3.orders.status.post.Response200 import (
    Response200 as Response200OrdersStatuses
)

from WB.marketplace.requestBodies.api.v3.orders.stickers.post.\
    RequestBody import RequestBody as OrdersForGetStickers
from WB.marketplace.responses.api.v3.orders.stickers.post.Response200 import (
    Response200 as Response200OrdersStickers,
)


from create_logger import create_logger

logger = create_logger(__name__)

LIMIT = 1000
load_dotenv()
api_key = os.getenv('WB_API_KEY')


def get_orders():
    next_ = 0
    date_from_unix = int(
        (datetime.datetime.now() - datetime.timedelta(3)).timestamp()
    )

    date_to_unix = int(datetime.datetime.now().timestamp())

    orders = []

    while True:

        response = ApiV3OrdersGet(api_key).execute(
            next=next_,
            limit=LIMIT,
            dateFrom=date_from_unix,
            dateTo=date_to_unix,
        )

        if not isinstance(response, Response200):
            logger.warning(response)
            break

        total = len(response.orders)
        orders += response.orders

        logger.info(f"{total} entries received. Total - {len(orders)}")

        if total < LIMIT:
            break

        next_ = response.next

    return orders


def get_new_orders():
    response = ApiV3OrdersNewGet(api_key).execute()

    if not isinstance(response, NewOrdersResponse200):
        logger.warning(response)
        return

    return response.orders


def get_orders_status(orders_ids: List[int]):
    response = ApiV3OrdersStatusPost(api_key).execute(
        OrdersForGetStatus(orders=orders_ids)
    )

    if not isinstance(response, Response200OrdersStatuses):
        logger.warning(response)
        return
    return response.orders


def get_orders_stickers(orders_ids: List[int]):
    if len(orders_ids) > 100:
        orders_ids = orders_ids[0:100]

    response = ApiV3OrdersStickersPost(api_key).execute(
        OrdersForGetStickers(orders=orders_ids),
        height=40,
        width=58,
        type="png"
    )

    if not isinstance(response, Response200OrdersStickers):
        logger.warning(response)
        return

    return response.stickers
