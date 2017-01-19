import logging
import log
from utils import id_generator

log.init()
logger = logging.getLogger('MAIN')


def run(login_information):
    user_ids = []
    for login in login_information:
        login_data = [data.strip() for data in login.split(',')]
        source = login_data[0]
        business = login_data[1]
        user_name = login_data[2]
        user_id = id_generator(source, business, user_name)
        user_ids.append(user_id)
        logger.info(user_id)


if __name__ == '__main__':
    logger.info('input:\n')
    login_information = []
    while True:
        input_line = input('>')
        if len(input_line.strip()) == 0:
            break
        login_information.append(input_line)

    result = run(login_information)
