"""unit-тесты для binary_re"""

import unittest

from binary_re import find_binary, find_binary_strict, is_binary, to_decimal


class TestIsBinary(unittest.TestCase):
    def test_digits_only(self):
        for text in ['0', '1', '1011', '0001']:
            with self.subTest(text=text):
                self.assertTrue(is_binary(text))
        for text in ['2', '102', '210']:
            with self.subTest(text=text):
                self.assertFalse(is_binary(text))
    def test_prefix(self):
        for text in ['0b1010', '0B101', '0b0']:
            with self.subTest(text=text):
                self.assertTrue(is_binary(text))
        for text in ['0b', '0B', '0b2']:
            with self.subTest(text=text):
                self.assertFalse(is_binary(text))
    def test_under(self):
        for text in ['1010_1100', '1_0_1', '0b_1100', '0b1_0']:
            with self.subTest(text=text):
                self.assertTrue(is_binary(text))
        for text in ['_1010', '10_', '1__0', '0b10_']:
            with self.subTest(text=text):
                self.assertFalse(is_binary(text))
    def test_no_signs(self):
        for text in ['-101', '+101', '10.1', '1.10']:
            with self.subTest(text=text):
                self.assertFalse(is_binary(text))
    def test_empty(self):
        for text in ['', ' 101', '101 ', '1 01']:
            with self.subTest(text=text):
                self.assertFalse(is_binary(text))

class TestFindBinary(unittest.TestCase):
    def test_separators(self):
        text = '101, 0b110 (101) и 11'
        self.assertEqual(find_binary(text), ['101', '0b110', '101', '11'])
    def test_inside_words_and_numbers(self):
        self.assertEqual(find_binary('абв101 и 102 и 2101'), [])
    def test_decimal(self):
        self.assertEqual(find_binary('10.5 и 5.10'), [])
    def test_no_binary(self):
        self.assertEqual(find_binary('здесь нет чисел 7 и 25'), [])
    def test_edges(self):
        text = '101 в начале и в конце 0b11'
        self.assertEqual(find_binary(text), ['101', '0b11'])
    def test_multiline(self):
        text = 'Регистр: 0b0000_0101\nСтатус: 1100\nОшибка: 7'
        self.assertEqual(find_binary(text), ['0b0000_0101', '1100'])
    def test_strict_mode(self):
        text = 'Регистр 0b0101, тел 101-01-01'
        self.assertEqual(find_binary(text), ['0b0101', '101', '01', '01'])
        self.assertEqual(find_binary_strict(text), ['0b0101'])

class TestToDecimal(unittest.TestCase):
    def test_values(self):
        cases = [('0', 0), ('1', 1), ('1010', 10),
                 ('0001', 1), ('0b1010_1100', 172)]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(to_decimal(text), expected)
    def test_invalid_raises(self):
        for text in [' 101', '-101', '102', '']:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    to_decimal(text)

if __name__ == '__main__':
    unittest.main()