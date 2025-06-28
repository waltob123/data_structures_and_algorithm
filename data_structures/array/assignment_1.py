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

    # First, check if the provided input is actually a list.
    # The test cases show that inputs could be other types like strings or integers.
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")

    # Check if the array is empty as per the requirements.
    # If it is, return (0, 0).
    if not array:
        return (0, 0)
    
    # Initialize both the minimum and maximum values with the first element of the array.
    # Before we do that, we must ensure the first element is an integer.
    if not isinstance(array[0], int):
        raise ValueError("Array must contain only integers")
        
    min_val = array[0]
    max_val = array[0]

    # Now, iterate through the rest of the array, starting from the second element.
    # We use array[1:] to create a slice of the array from the second element to the end.
    for number in array[1:]:
        
        # At each step, validate that the element is an integer.
        # If not, raise a ValueError as required.
        if not isinstance(number, int):
            raise ValueError("Array must contain only integers")

        # Check if the current number is greater than our current maximum.
        # If it is, we update our maximum value.
        if number > max_val:
            max_val = number
        
        # Check if the current number is less than our current minimum.
        # If it is, we update our minimum value.
        elif number < min_val:
            min_val = number

    # After the loop has finished, return the final minimum and maximum values in a tuple.
    return (min_val, max_val)
