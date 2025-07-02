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


def def_sum_array(*, array: list[int]) -> int:
    """
    Calculate the sum of all elements in a list of integers.

    Parameters:
        array (list[int]): The list of integers to sum.

    Returns:
        int: The total sum of the elements in the array.

    Raises:
        ValueError: If the list contains non-integer values.
    """

    # Check if the input is a list
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")

    # Validate all elements in the list are integers
    for value in array:
        if not isinstance(value, int):
            raise ValueError("Array must contain only integer")

    # Returns 0 if the list is empty
    if not array:
        return 0

    # Return the single element if the list has only one item
    if len(array) == 1:
        return array[0]

    # Initializing a variable to hold the total sum
    total = 0

    # Loop through each number in the array and add to total
    for number in array:
        total += number

    # Return the final total sum
    return total

def def_reverse_array(*, array: list[int]) -> list[int]:
    """
    Reverse the elements of an array of integers and return the reversed array.

    Parameters:
        array (list[int]): The list of integers to reverse.

    Returns:
        list[int]: A new list with elements in reverse order.

    Raises:
        ValueError: If the list contains non-integer values.
    """

    # Check if the input is a list
    if not isinstance(array, list):
        raise ValueError("Array must contain only integer")

    # Validate all elements in the list are integers
    for value in array:
        if not isinstance(value, int):
            raise ValueError("Array must contain only integer")

    # Return an empty list if the input list is empty
    if not array:
        return []

    # If the list has only one element, return it as is
    if len(array) == 1:
        return array

    # Initialize an empty list to store reversed elements
    reversed_array = []

    # Loop through the list from the end to the beginning
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])  # Append elements in reverse order

    # Return the reversed array
    return reversed_array   
