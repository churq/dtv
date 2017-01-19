class BaseError(Exception):
    code = -1
    message = ''

class InvalidCompanyName(BaseError):
    code = 2
    message = 'company name is not in whitelisted'

class InvalidSource(BaseError):
    code = 3
    message = 'Invalid source'



