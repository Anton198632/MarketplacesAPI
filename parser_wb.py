from WB.parser import WBParser
from create_logger import create_logger

logger = create_logger(__name__)

if __name__ == "__main__":
    sections = [
        "prices",
        "content",
        "supplies",
        "marketplace",
        "statistics",
        "analytics",
        "promotion",
        "recommendations",
        "feedbacks-questions",
        "tariffs",
        "buyers-chat",
        "returns",
    ]

    for section in sections:
        logger.info(f'Parsing section "{section}"...')
        parser = WBParser(section)
        parser.parse_wb_api()

    logger.info("Completed")

