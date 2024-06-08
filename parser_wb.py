from WB.parser import WBParser


if __name__ == "__main__":
    sections = ["content", "prices"]

    for section in sections:
        parser = WBParser(section)
        parser.parse_wb_api()
        pass
