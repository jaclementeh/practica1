import os
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")

file_handler = logging.FileHandler('../outputfiles/emptyfiles.log', 'w', 'utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def empty_file(file):

    if os.path.getsize(file) > 0:
        logger.debug("Data in file")
    else:
        logger.warning("NO Data in file")

