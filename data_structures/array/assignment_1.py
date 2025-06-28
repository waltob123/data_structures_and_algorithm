'''
Author: Desmond Asiedu Asamoah
Date: 2025-06-27
Description: This module provides a simple implementation of an array data structure.
'''


'''
Question 1.
- Find the maximum and minimum values in an array of integers.
- Return a tuple containing the minimum and maximum values with the minimum value first.
- If the array is empty, return (0, 0).
- If the array contains only one element, return that element as both the minimum and maximum.
- If the array does not contain numbers or not empty, raise a ValueError with the message "Array must contain only integers".
- Comment every step in your code.
- Leave whitespace where appropriate.
- Do not use the in-built min and max functions.
- Do not use sorted or array.sort() methods.
'''

ARRAY_INTEGER_VALIDATION_ERROR = 'Array must be integers only!'
EMPTY_ARRAY_VALUE_ERROR = 'The array is empty.'

def find_min_max_in_array(*, array: list[int]) -> tuple[int, int]:
    """
    Find the minimum and maximum values in an array.

    :param array: A array of integers.

    :return: A tuple containing the minimum and maximum values, with the minimum value first.
    """
    # Validate input list
    if not isinstance(array, list):
        raise ValueError(ARRAY_INTEGER_VALIDATION_ERROR)
    
    # Validate array as  int
    for item in array:
        if not isinstance(item, int):
            raise ValueError(ARRAY_INTEGER_VALIDATION_ERROR)
    
    # Empty list case
    if len(array) == 0:
        print(EMPTY_ARRAY_VALUE_ERROR)
        return (0, 0)
    
    min_val = array[0]
    max_val = array[0]
    
    for value in array[1:]:
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    
    return (min_val, max_val)

test_array = [7, 5, 1, 3, 5, 0, 9, 10]
# integer array
print(find_min_max_in_array(array=test_array))

# single & empty element array
print(find_min_max_in_array(array=[42]))
print(find_min_max_in_array(array=[]))

# invalid input criteria
try:
    find_min_max_in_array(array=["Ghana", "Accra"])
except ValueError as e:
    print(e)