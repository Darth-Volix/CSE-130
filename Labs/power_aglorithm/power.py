# 1. Name:
#      Nicholas Wilkins
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program reads an array from a JSON file and finds the highest average of all subarrays of a given length.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was ensuring that the program could handle all possible exceptions that could occur when   
#      reading the JSON file and finding the highest average of a subarray. I still find it hard to think about all
#      the possible exceptions that could occur and how to handle them. Making sure the program did all of that and
#      still was readable and understandable was difficult. I am a bit of a perfectionist and I want to make sure that
#      my code is as clean and efficient as possible. Comments are quickly becoming my best friend. 
# 5. How long did it take for you to complete the assignment?
#      It took me about 2 hours to complete this assignment.

import json

def json_reader(file_name):
    '''
    Read a JSON file and return the array.

    Parameters:
        file_name (str): The name of the JSON file.

    Returns:
        array: The array read from the JSON file.
    '''
    assert isinstance(file_name, str), "The file name should be a string."

    try:
        # Attempt to open the file.
        with open(file_name, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")
    except json.JSONDecodeError:
        raise ValueError("The file is not in a valid JSON format.")

    # Ensure the 'array' key exists in the JSON data.
    if 'array' not in data:
        raise KeyError("The JSON file does not have 'array' as a key.")

    array = data['array']

    # Ensure that the data in "array" is a list.
    assert isinstance(array, list), "The data read from the file should be a list."

    # Ensure that all elements in the array are integers.
    if not all(isinstance(i, int) for i in array):
        raise ValueError("All elements in the 'array' should be integers.")

    return array

def find_highest_subarray_average(array, subarray_length):
    '''
    This function finds the highest average of a subarray of a given length in a given array.

    Parameters:
        array (list): The input array.
        subarray_length (int): The length of the subarray.

    Returns:
        float: The highest average of a subarray of length subarray_length.
    '''
    assert isinstance(array, list), "Input array must be a list."
    assert all(isinstance(i, int) for i in array), "All elements in the input array must be integers."
    assert isinstance(subarray_length, int), "Subarray length must be an integer."
    assert subarray_length > 0, "Subarray length must be a positive integer."
    assert subarray_length <= len(array), "Subarray length must not exceed the length of the input array."

    # Initialize the highest average and set it to negative infinity.
    highest_average = float('-inf')

    # Iterate through the main array, starting at each index and ending at the last index where a subarray 
    # of length subarray_length can be formed.
    for starting_index in range(len(array) - subarray_length + 1):
        subarray_sum = 0

        # Calculate the sum of the subarray.
        for i in range(starting_index, starting_index + subarray_length):
            subarray_sum += array[i]

        # Calculate the average of the subarray.
        average = subarray_sum / subarray_length

        # Update the highest average if the current average is greater.
        if average > highest_average:
            highest_average = average

    return highest_average


def main():
    try:
        file_name = input("\nEnter the JSON file name: ")
        array = json_reader(file_name)
    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"Invalid Input: {e}\n")
        return
    except AssertionError as e:
        print(f"Assertion Error: {e}\n")
        return

    try:
        subarray_length = int(input("Enter the size of the subarray: "))
        if subarray_length <= 0:
            raise ValueError("Subarray length must be a positive integer.")
        elif subarray_length > len(array):
            raise ValueError("Subarray length must not exceed the length of the input array.")  
    except ValueError as e:
        print(f"Invalid Input: {e}\n")
        return
    
    try:
        highest_average = find_highest_subarray_average(array, subarray_length)
        print(f"The highest average of a subarray of length {subarray_length} is: {highest_average}\n")
    except AssertionError as e:
        print(f"Assertion Error: {e}\n")
        return

if __name__ == "__main__":
    main()

