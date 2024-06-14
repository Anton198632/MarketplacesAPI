<h1>MarketplacesAPI</h1>

The program is designed to generate scripts and classes in Python for using the open APIs of the Wildberries and Ozon marketplaces (under development). It is essentially an HTTP request wrapper and response deserializer.
<br>

## Install

- Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
- To generate after version of the marketplace API, run the appropriate script. For example for Wildberries:
```bash
python parser_wb.py
```
- Set API keys obtained from marketplace sites to variables to access the use of the API. For example for Wildberry:
```
WB_API_KEY: eyJhbGci********V6qnvoLBImYg
```
You can also create a **.env** file in which you can register the API keys:
```
WB_API_KEY=eyJhbGci********V6qnvoLBImYg
```
## Example

The script below allows you to get a list of created NMs with filtering by various parameters, pagination and sorting.
<br>
*Link to the method in the marketplace manual:* [Список номенклатур (НМ)](https://openapi.wb.ru/content/api/ru/#tag/Prosmotr/paths/~1content~1v2~1get~1cards~1list/post)

```python
import os

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

api_key = os.getenv("WB_API_KEY")

cursor = RequestBodySettingsCursor(limit=100)
request = ContentV2GetCardsListPost(api_key)

response = request.execute(
    body_request=RequestBody(
        settings=RequestBodySettings(
            sort=RequestBodySettingsSort(True),
            filter=RequestBodySettingsFilter(withPhoto=-1),
            cursor=cursor,
        ),
    ),
)

```