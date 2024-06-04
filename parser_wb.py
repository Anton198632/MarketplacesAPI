from WB.parser import WBParser

if __name__ == "__main__":
    # sections = ["content", "prices"]
    #
    # for section in sections:
    #     wb_api_content = get_wb_api(section)
    #     dict_write(f"WB/content/parser/wb_api_{section}.json", wb_api_content)

    parser = WBParser("prices")

    parser.parse_wb_api()

