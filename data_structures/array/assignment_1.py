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

'''
Question 2
Reverse an array (without using built-in reverse)
Return a new array with the elements in reverse order.
- If the array is empty, return an empty array.
- If the array contains only one element, return the array as is.
- If the array does not contain numbers or is not empty, raise a ValueError with the message "Array must contain only integers".
- Do not use the in-built reversed function or array.reverse() method.
- Comment every step in your code.
- Leave whitespace where appropriate.'''

def reverse_array(*, array: list[int]) -> list[int]:
    """
    Reverse an array.

    :param array: A array of integers.
    :return: A new array with the elements in reverse order.
    """
    # Check if array is empty and this returns an empty list
    if not array:
        return []
    
    # Check if array is a list, raise ValueError if not
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")
    
    # Check if all elements are integers
    for item in array:
        if not isinstance(item, int):
            raise ValueError("Array must contain only integers")
    
    # If array has only one element, return a new copy of the array
    if len(array) == 1:
        return array.copy()
    
    # Initialize a new array with the same length as the input array
    reversed_array = [0] * len(array)
    
    # Iterate through the input array and populate the new array in reverse order
    for i in range(len(array)):
        reversed_array[len(array) - 1 - i] = array[i]
    
    # Return the new reversed array
    return reversed_array

"""
Question 3
- Calculate the sum of all elements in an array.
- Return the sum.
- If the array is empty, return 0.
- If the array contains one element, return the element.
- If the array does not contain numbers or is not empty, raise a ValueError with the message "Array must contain only integers".
- Do not use the in-built sum function.
- Comment every step in your code.
- Leave whitespace where appropriate.
"""
def sum_of_array(*, array: list[int]) -> int:
    """    Calculate the sum of all elements in an array.

    :param array: A array of integers.
    :return: The sum of all elements in the array.
    """
    # Check if array is empty and return 0
    if not array:
        return 0
    
    # Check if array is a list, raise ValueError if not
    if not isinstance(array, list):
        raise ValueError("Array must contain only integers")
    
    # Check if all elements are integers
    for item in array:
        if not isinstance(item, int):
            raise ValueError("Array must contain only integers")
    
    # If array has only one element, return that element
    if len(array) == 1:
        return array[0]
    
    # Initialize sum variable
    total_sum = 0
    
    # Iterate through the array and accumulate the sum
    for num in array:
        total_sum += num
    
    # Return the total sum
    return total_sum
