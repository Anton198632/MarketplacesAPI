# from WB.content.ContentV2GetCardsListPost import ContentV2GetCardsListPost
# from WB.content.requestBodies.content.v2.get.cards.list.post.RequestBody import \
#     RequestBody
# from WB.content.requestBodies.content.v2.get.cards.list.post.RequestBodySettings import \
#     RequestBodySettings
# from WB.content.requestBodies.content.v2.get.cards.list.post.RequestBodySettingsCursor import \
#     RequestBodySettingsCursor
# from WB.content.requestBodies.content.v2.get.cards.list.post.RequestBodySettingsFilter import \
#     RequestBodySettingsFilter
# from WB.content.requestBodies.content.v2.get.cards.list.post.RequestBodySettingsSort import \
#     RequestBodySettingsSort

from WB.parser import WBParser
from WB.serializers import from_dict

if __name__ == "__main__":
    sections = ["prices", "content"]

    # api_key = ""

    # result = ContentV2GetCardsListPost(api_key).execute(
    #     RequestBody(
    #         RequestBodySettings(
    #             RequestBodySettingsSort(True),
    #             RequestBodySettingsFilter(withPhoto=-1,),
    #             RequestBodySettingsCursor(limit=100)
    #         )))

    for section in sections:
        parser = WBParser(section)
        parser.parse_wb_api()
        pass
