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

    #check if array is empty
    if not array:
     return (0, 0)
    
    #check if all elements are of type integer
    for item in array:
        if not isinstance(item, int):
           raise ValueError("the item is not an integer")

    #if array has only one element, return it as both min and max    
    if len(array)==1:
       return(array[0], array[0])
    
   #initialize min and max with first elements in the list 
    maximum_number = array[0]
    minimum_number = array[0]
    
    #iterate through the array starting from second element (sliced)
    for num in array[1:]:
       
       #update minimum if current number is smaller
       if num < minimum_number:
           minimum_number= num

       #update maximum if current number is larger or bigger       
       if num > maximum_number:
            maximum_number =num

#return tuple with minimum first, then maximum
    return (minimum_number, maximum_number)