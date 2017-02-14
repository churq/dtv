class CertificateBaseError(Exception):
    code = -1
    message = ''

class InvalidCompanyName(CertificateBaseError):
    code = 2
    message = 'company name is not in whitelisted'



