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


'''
Question 2
Reverse an array (without using built-in reverse)
Return a new array with the elements in reverse order.
- If the array is empty, return an empty array.
- If the array contains only one element, return the array as is.
- If the array does not contain numbers or is not empty, raise a ValueError with the message "Array must contain only integers".
- Do not use the in-built reversed function or array.reverse() method.
- Comment every step in your code.
- Leave whitespace where appropriate.
'''
def reverse_array(*, array: list[int]) -> list[int]:
    """
    Reverse an array.

    :param array: A array of integers.

    :return: A new array with the elements in reverse order.
    """


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
    """
    Sum the elements of an array.

    :param array: An array of integers.

    :return: The sum of the elements in the array.
    """
