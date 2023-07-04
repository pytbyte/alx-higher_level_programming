import unittest
from max_integer import max_integer

class MaxIntegerTest(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 2, -3, 4, -5])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        result = max_integer([1, 2, 2, 3, 3, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_single_number(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.7, 3.2, 4.9, 5.1])
        self.assertEqual(result, 5.1)

    def test_mixed_integer_float_list(self):
        result = max_integer([1, 2, 3.5, 4, 5])
        self.assertEqual(result, 5)

    def test_empty_default_list(self):
        result = max_integer()
        self.assertIsNone(result)

    def test_string_elements(self):
        result = max_integer(['apple', 'banana', 'cherry'])
        self.assertIsNone(result)

    def test_boolean_elements(self):
        result = max_integer([True, False, True])
        self.assertIsNone(result)

    def test_none_elements(self):
        result = max_integer([None, None, None])
        self.assertIsNone(result)

    def test_empty_sublist(self):
        result = max_integer([[], [1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, [4, 5, 6])

    def test_list_with_none_sublist(self):
        result = max_integer([[1, 2, 3], None, [4, 5, 6]])
        self.assertEqual(result, [4, 5, 6])

    def test_list_with_different_types_sublist(self):
        result = max_integer([[1, 2, 3], 'abc', [4, 5, 6]])
        self.assertIsNone(result)

    def test_list_with_mixed_integer_float_sublist(self):
        result = max_integer([[1, 2, 3], [4.5, 5.5, 6.5], [7, 8, 9]])
        self.assertEqual(result, [7, 8, 9])

if __name__ == '__main__':
    unittest.main()
