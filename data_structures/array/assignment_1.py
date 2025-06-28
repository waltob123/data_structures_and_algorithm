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
def find_min_max_in_array(*, array: list[int]) -> tuple[int, int]:
    """
    Find the minimum and maximum values in an array.

    :param array: A array of integers.
    :return: A tuple containing the minimum and maximum values, with the minimum value first.
    """
    # Check if array is empty
    if not array:
        return (0, 0)
    
    # Check if array is a list, raise ValueError if not
    if not isinstance(array, list):
        raise ValueError("Array must be a list of integers")
    
    # Check if all elements are integers
    for item in array:
        if not isinstance(item, int):
            raise ValueError("Array must contain only integers")
    
    # If array has only one element, return it as both min and max
    if len(array) == 1:
        return (array[0], array[0])
    
    # Initialize min and max with first element
    minimum_number = array[0]
    maximum_number = array[0]
    
    # Iterate through array starting from second element
    for num in array[1:]:
        # Update minimum if current number is smaller
        if num < minimum_number:
            minimum_number = num
        # Update maximum if current number is larger
        if num > maximum_number:
            maximum_number = num
    
    # Return tuple with minimum first, then maximum
    return (minimum_number, maximum_number)