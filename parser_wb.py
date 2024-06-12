from WB.parser import WBParser


if __name__ == "__main__":
    sections = [
        # "prices",
        # "content",
        # "supplies",
        # "marketplace",
        # "statistics",
        "analytics",
        # "promotion",
        # "recommendations",
        # "feedbacks-questions",
        # "tariffs",
        # "buyers-chat",
        # "returns",
    ]

    for section in sections:
        parser = WBParser(section)
        parser.parse_wb_api()
        pass
