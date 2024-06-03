import logging

import colorlog


def create_logger(name):
    logger = colorlog.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для вывода логов в stdout с цветами
    stdout_handler = colorlog.StreamHandler()
    stdout_handler.setFormatter(
        colorlog.ColoredFormatter(
            (
                "%(log_color)s%(asctime)s - %(name)s - %(levelname)s"
                " - %(message)s"
            ),
            datefmt="%d.%m.%Y %H:%M:%S",
            log_colors={
                "DEBUG": "bg_cyan,white",
                "INFO": "bold_green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bg_red,fg_light_white",
            },
            secondary_log_colors={},
        )
    )

    # Добавляем обработчик к логгеру
    logger.addHandler(stdout_handler)

    return logger
