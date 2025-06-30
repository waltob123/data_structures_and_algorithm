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
    Find the minimum and maximum values in a list of integers.

    Parameters:
        array (list[int]): The list of integers to process.

    Returns:
        tuple[int, int]: A tuple with the minimum value first, then the maximum.

    Raises:
        ValueError: If the list is not empty but contains non-integer values.
    """

    # Checks if the list is empty
    if not array:
        return (0, 0)
    
    #validate if array is a list and then raise vlaue error
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")


    # Validate all elements are integers
    for value in array:
        if not isinstance(value, int):
            raise ValueError("Array must contain only integers")
        
    # Checks if the list has only one element
    if len(array) == 1:
        return (array[0], array[0])

    # Initialize min and max
    min_val = array[0]
    max_val = array[0]

    # Loop through remaining elements
    for i in range(1, len(array)):
        current = array[i]
        if current < min_val:
            min_val = current
        if current > max_val:
            max_val = current

    return (min_val, max_val)


