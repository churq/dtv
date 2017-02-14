import logging

logger = logging.getLogger('Encoding Engine')


class Hash(object):
    """
    This class is to encode the string to a unique ID
    """
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    def __init__(self,hashed_length):
        self._hashed_length = hashed_length

    def _verification(self, input_string):
        """
        This method is to verify the input string is all ASCII

        Args:
            input_string:

        Returns: boolean

        """
        if not isinstance(input_string, str):
            logger.error('can not be encoded, input is not string')
            return

    def encode(self, original_str):
        if not self._verification(original_str):
            return


    def _hash_function(self, input_str):
        encoded_string_raw = [self.encode_character(char) for char in input_str]



class IDGenerator(object):
    def __init__(self, company_code, login_source_code, username):
        self._company_code = company_code
        self._login_source_code = login_source_code
        self._username = username

