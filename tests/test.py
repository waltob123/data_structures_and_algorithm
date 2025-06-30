import inspect
import unittest

#from data_structures.array.assignment_1 import find_min_max_in_array
from data_structures.array.assignment_1 import find_min_max_in_array, reverse_array, sum_of_array

class TestArray(unittest.TestCase):
    def setUp(self):
        self.array = [7, 5, 1, 3, 5, 0, 9, 10, 4, 34, 23, 64, 89, 12]
        self.empty_array = []
        self.value = 9
        self.random_string = "random_string"
        self.string_array = ["apple", "banana", "cherry", "date", "elderberry"]
        self.mixed_array = [1, "two", 3.0, "four", 5]
        self.float_array = [1.5, 2.3, 3.7, 4.1, 5.6]
        self.single_element_array = [42]
        self.negative_numbers_array = [-10, -20, -30, -40, -50]

    def tearDown(self):
        del self.array
        del self.empty_array
        del self.value
        del self.random_string

    def test_find_min_max_in_array_with_valid_array(self):
        result = find_min_max_in_array(array=self.array)
        self.assertEqual(result, (0, 89))

    def test_find_min_max_in_array_with_empty_array(self):
        result = find_min_max_in_array(array=self.empty_array)
        self.assertEqual(result, (0, 0))

    def test_find_min_max_in_array_with_single_element(self):
        result = find_min_max_in_array(array=self.single_element_array)
        self.assertEqual(result, (42, 42))

    def test_find_min_max_in_array_with_negative_numbers(self):
        result = find_min_max_in_array(array=self.negative_numbers_array)
        self.assertEqual(result, (-50, -10))

    def test_find_min_max_in_array_with_string_array(self):
        with self.assertRaises(ValueError) as err:
            find_min_max_in_array(array=self.string_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_find_min_max_in_array_with_mixed_array(self):
        with self.assertRaises(ValueError) as err:
            find_min_max_in_array(array=self.mixed_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_find_min_max_in_array_with_float_array(self):
        with self.assertRaises(ValueError) as err:
            find_min_max_in_array(array=self.float_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_find_min_max_in_array_with_random_string(self):
        with self.assertRaises(ValueError) as err:
            find_min_max_in_array(array=self.random_string)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_find_min_max_in_array_with_value(self):
        with self.assertRaises(ValueError) as err:
            find_min_max_in_array(array=self.value)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_reverse_array_with_valid_array(self):
        result = reverse_array(array=self.array)
        self.assertEqual(result, list(reversed(self.array)))    

    def test_reverse_array_with_empty_array(self):
        result = reverse_array(array=self.empty_array)
        self.assertEqual(result, [])

    def test_reverse_array_with_single_element(self):
        result = reverse_array(array=self.single_element_array)
        self.assertEqual(result, self.single_element_array)

    def test_reverse_array_with_string_array(self):
        with self.assertRaises(ValueError) as err:
            reverse_array(array=self.string_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_reverse_array_with_mixed_array(self):
        with self.assertRaises(ValueError) as err:
            reverse_array(array=self.mixed_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_reverse_array_with_float_array(self):
        with self.assertRaises(ValueError) as err:
            reverse_array(array=self.float_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_reverse_array_with_random_string(self):
        with self.assertRaises(ValueError) as err:
            reverse_array(array=self.random_string)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_reverse_array_with_value(self):
        with self.assertRaises(ValueError) as err:
            reverse_array(array=self.value)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_sum_of_array_with_valid_array(self):
        result = sum_of_array(array=self.array)
        self.assertEqual(result, sum(self.array))

    def test_sum_of_array_with_empty_array(self):
        result = sum_of_array(array=self.empty_array)
        self.assertEqual(result, 0)

    def test_sum_of_array_with_single_element(self):
        result = sum_of_array(array=self.single_element_array)
        self.assertEqual(result, 42)

    def test_sum_of_array_with_negative_numbers(self):
        result = sum_of_array(array=self.negative_numbers_array)
        self.assertEqual(result, -150)

    def test_sum_of_array_with_string_array(self):
        with self.assertRaises(ValueError) as err:
            sum_of_array(array=self.string_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_sum_of_array_with_mixed_array(self):
        with self.assertRaises(ValueError) as err:
            sum_of_array(array=self.mixed_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_sum_of_array_with_float_array(self):
        with self.assertRaises(ValueError) as err:
            sum_of_array(array=self.float_array)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_sum_of_array_with_random_string(self):
        with self.assertRaises(ValueError) as err:
            sum_of_array(array=self.random_string)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_sum_of_array_with_value(self):
        with self.assertRaises(ValueError) as err:
            sum_of_array(array=self.value)
            self.assertEqual(err.msg, "Array must contain only integers")

    def test_function_signature(self):
        # check if min and max, sorted or array.sort in-built functions are not used
        min_max_source_code = inspect.getsource(find_min_max_in_array)
        reverse_source_code = inspect.getsource(reverse_array)
        sum_source_code = inspect.getsource(sum_of_array)
        self.assertNotIn("min(", min_max_source_code)
        self.assertNotIn("max(", min_max_source_code)
        self.assertNotIn("sorted(", min_max_source_code)
        self.assertNotIn("array.sort(", min_max_source_code)
        self.assertNotIn("reversed(", reverse_source_code)
        self.assertNotIn("array.reverse(", reverse_source_code)
        self.assertNotIn("sum(", sum_source_code)


if __name__ == "__main__":
    unittest.main()