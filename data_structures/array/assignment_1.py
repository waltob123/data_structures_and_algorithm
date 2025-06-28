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
        integers (list[int]): The list of integers to process.

    Returns:
        tuple[int, int]: A tuple with the minimum value first, then the maximum.

    Raises:
        ValueError: If the list is not empty but contains non-integer values.
    """

    # Checks if the list is empty
    if not array:
        return (0, 0)

    # Checks if the list has only one element
    if len(array) == 1:
        return (array[0], array[0])

    # loops through each item in the list and raise an error and stops if any element is not an integer
    for value in array:
        if not isinstance(value, int):
            raise ValueError("Array must contain only integers")

    # sets min_val and max_val to the first element.(also helps in returning same if there is only one element)
    min_val = array[0]
    max_val = array[0]

    # Loops through the list starting from the second element
    for i in range(1, len(array)):
        current = array[i]

        # Update min if current is smaller
        if current < min_val:
            min_val = current

        # Update max if current is larger
        if current > max_val:
            max_val = current

    # Return result as a tuple
    return (min_val, max_val)


# ---------------------------------------------
# Main program start from here

# Create a list of 60 integers from 1 to 60
integerz = []

for i in range(1, 61):
    integerz.append(i)

# Call the function using keyword argument
result = find_min_max_in_array(array=integerz)

# Print the result
print("Minimum and Maximum values:", result)

