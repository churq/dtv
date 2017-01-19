import logging
import log
from configuration.settings import (
    SOURCE_TABLENAME, COMPANY_TABLENAME
)
from db_setup import acquire_code

logger = logging.getLogger('UTILS')
log.init()


class Hash(object):
    """
    This class is to encode the string to a unique ID
    """
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    HASHED_LEN = 6

    def __init__(self, alphabet=ALPHABET, hashed_length=HASHED_LEN):
        self._alphabet = alphabet
        self._hashed_len = hashed_length
        self._start_index = None

    @property
    def hashedvalue_len(self):
        return 8

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

        if not self._is_ascii(input_string):
            logger.error('can not be encoded, input has to be ASCII')
            return

        return True

    def encode(self, original_str):
        if not self._verification(original_str):
            return

        return self._hash_function(original_str)

    def _extend_str(self, input_str):
        if len(input_str) < self._hashed_len:
            while len(input_str) < self._hashed_len:
                input_str = input_str * 2
        return input_str[:self._hashed_len]

    def _hash_function(self, input_str):
        if len(input_str) < self._hashed_len:
            input_str = self._extend_str(input_str)

        encoded_str = [''] * self._hashed_len
        start_index = self._decide_start_index(input_str)
        for char in input_str:
            if '' not in encoded_str:
                break
            encoded_str[start_index] = self._encode_function(char)
            if start_index == self._hashed_len - 1:
                start_index = 0
            else:
                start_index += 1
        unhashed_char = input_str[self._hashed_len - len(input_str):]
        for char in unhashed_char:
            new_str = unhashed_char + ''.join(encoded_str)
            replaced_index = self._decide_start_index(new_str)
            encoded_str[replaced_index] = self._encode_function(char)

        return ''.join(encoded_str)

    def _encode_function(self, original_char):
        """
        This function is to encode the alphanumeric character
        by mapping 'alphabet_ord' into self._alphabet

        Args:
            original_char:

        Returns: encoded alphanumeric


        """
        start_index = int(len(self._alphabet) / 2)
        # put all the ASCII value of [0-9a-zA_Z] in the list
        alphabet_ord = list(range(48, 58)) + list(range(97, 123)) + list(range(65, 91))
        if ord(original_char) not in alphabet_ord:
            return

        if ord(original_char) in alphabet_ord:
            for ord_value in alphabet_ord:
                if ord_value == ord(original_char):
                    return self._alphabet[start_index]

                if start_index == len(self._alphabet) - 1:
                    start_index = 0
                else:
                    start_index += 1

    def _decide_start_index(self, input_str):
        first_hashed = [
            (self._alphabet.index(char), self._alphabet.index(char) % self.hashedvalue_len)
            for char in input_str]
        second_hashed = sum((item[0] * item[1] + 1) ** 3 for item in first_hashed)
        start_index = second_hashed % self._hashed_len
        return start_index

    def _is_ascii(self, input_string):
        return all(ord(char) < 128 for char in input_string)


def id_generator(source, company, username):
    source_code = acquire_code(SOURCE_TABLENAME, source)
    company_code = acquire_code(COMPANY_TABLENAME, company)
    if not source_code or not company_code:
        logger.error('invalid business name or source name')
        return 'error'

    hashid = Hash()
    username_code = hashid.encode(username)
    return company_code + source_code + username_code
