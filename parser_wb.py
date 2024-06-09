from WB.parser import WBParser


if __name__ == "__main__":
    sections = ["prices", "content"]

    for section in sections:
        parser = WBParser(section)
        parser.parse_wb_api()
        pass
