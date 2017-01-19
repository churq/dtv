import unittest
from nose_parameterized import parameterized
from utils import Hash


class TestHash(unittest.TestCase):
    @parameterized.expand([
        # ('a', 0),
        # ('ai', 2),
        # ('a0', 0),
        ('jess0000', 1),
        ('jess0001', 4)
    ])
    def test_decide_start_index(self, input_str, result):
        hash = Hash()
        start_index = hash._decide_start_index(input_str)
        self.assertEquals(start_index, result)

    @parameterized.expand([
        ('a', 'P'),
        ('b', 'Q'),
        ('0', 'F'),
        ('9', 'O'),
        ('-', None),
    ])
    def test_encode_function(self, input_char, encoded_result):
        hash_ = Hash()
        encoded = hash_._encode_function(input_char)
        self.assertEquals(encoded, encoded_result)

    @parameterized.expand([
        ('abc', 'abcabc'),
        ('chu01', 'chu01c')
    ])
    def test_extend_str(self, input_str, result):
        hash_ = Hash()
        extended_str = hash_._extend_str(input_str)
        self.assertEqual(extended_str, result)

    @parameterized.expand([
        ('jess0001', '7GFFFT'),
        ('jess0002', 'HFFFT7'),
        ('joe4444', 'JJY3TJ'),
        ('rachel01', 'FPRWTG'),

    ])
    def test_hashed_function(self, input_str, hashed_result):
        hash_ = Hash()
        for i in range(0,3):
            hashed = hash_._hash_function(input_str)
            self.assertEqual(hashed, hashed_result)