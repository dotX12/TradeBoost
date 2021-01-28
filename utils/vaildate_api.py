from logger.logger_module import logger


def validate_api_response(response):
    if list(response.keys())[0] != 'strError':
        return True
    else:
        key = list(response.keys())[0]
        logger.warning(f'Error - {response[key]}')
        return response[key]
