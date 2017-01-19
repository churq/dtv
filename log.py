import logging
from configuration import settings

from configuration.settings import LOG_DIR


def init():
    level_mode = logging.DEBUG if settings.DEBUG else logging.INFO
    logging.basicConfig(level=level_mode)
    logger = logging.getLogger()
    logger_matching_engine = logging.getLogger('DATABASE')
    logger_matching_engine.setLevel(logging.INFO)

    logger_redshift = logging.getLogger('MAIN')
    logger_redshift.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        LOG_DIR + '/' + 'output.log', mode='w')
    formatter = logging.Formatter(
        '%(asctime)s%(name)s:%(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    error_file_handler = logging.FileHandler(
        LOG_DIR + '/' + 'error.log', mode='a')

    error_file_handler.setFormatter(formatter)
    error_file_handler.setLevel(logging.ERROR)
    logger.addHandler(error_file_handler)
