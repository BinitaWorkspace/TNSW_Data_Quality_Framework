import logging
import os
from datetime import datetime


def get_logger(name):

    log_folder = "logs"

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    log_file = os.path.join(
        log_folder,
        f"data_quality_{datetime.now().strftime('%Y%m%d')}.log"
    )

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:

        file_handler = logging.FileHandler(log_file)

        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger