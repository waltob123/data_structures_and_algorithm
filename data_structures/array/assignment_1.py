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

    :param array: An array of integers.

    :return: A tuple containing the minimum and maximum values, with the minimum value first.
    """

    # First, validate that the input itself is a list.
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")

    # Check if the array is empty as per the requirements.
    if not array:
        return (0, 0)
    
    # Perform a validation to ensure all elements in the list are integers.
    for item in array:
        if not isinstance(item, int):
            raise ValueError("Array must contain only integers")

    # If validation is successful, proceed to find the min and max.
    # Initialize with the first element, since we know the list is not empty.
    min_val = array[0]
    max_val = array[0]

    # Iterate from the second element to the end.
    for number in array[1:]:
        
        # Check if the current number is greater than our current maximum.
        if number > max_val:
            max_val = number
        
        # Check if the current number is less than our current minimum.
        elif number < min_val:
            min_val = number

    # After the loop has finished, return the final minimum and maximum values in a tuple.
    return (min_val, max_val)

'''
Question 2
- Reverse an array (without using built-in reverse)
- ...
'''
def reverse_array(*, array: list[int]) -> list[int]:
    """
    Reverse an array.

    :param array: An array of integers.
    :return: A new array with the elements in reverse order.
    """
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")

    if not array:
        return []

    for item in array:
        if not isinstance(item, int):
            raise ValueError("Array must contain only integers")

    reversed_list = array[::-1]

    return reversed_list


"""
Question 3
- Calculate the sum of all elements in an array.
- ...
"""
def sum_of_array(*, array: list[int]) -> int:
    """
    Sum the elements of an array.

    :param array: An array of integers.
    :return: The sum of the elements in the array.
    """
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")

    for item in array:
        if not isinstance(item, int):
            raise ValueError("Array must contain only integers")

    total_sum = 0
    for number in array:
        total_sum += number

    return total_sum