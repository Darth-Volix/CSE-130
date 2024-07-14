import json

def json_reader(file_name):
    '''
    Read a JSON file and return the array.

    Parameters:
        file_name (str): The name of the JSON file.

    Returns:
        array: The array read from the JSON file.
    '''
    assert isinstance(file_name, str), "The file name should be a string.\n"

    try:
        # Attempt to open the file
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_name}' does not exist.\n")
    except json.JSONDecodeError:
        raise ValueError("The file is not in a valid JSON format.\n")

    # Ensure the 'array' key exists in the JSON data
    if 'array' not in data:
        raise KeyError("The JSON file does not have 'array' as a key.\n")

    array = data['array']

    # Ensure that the data in "array" is a list
    assert isinstance(array, list), "The data read from the file should be a list.\n"

    # Ensure that all elements in the array are integers
    if not all(isinstance(i, int) for i in array):
        raise ValueError("All elements in the 'array' should be integers.\n")

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
    assert isinstance(array, list), "Input array must be a list.\n"
    assert all(isinstance(i, int) for i in array), "All elements in the input array must be integers.\n"
    assert isinstance(subarray_length, int), "Subarray length must be an integer.\n"
    assert subarray_length > 0, "Subarray length must be a positive integer.\n"
    assert subarray_length <= len(array), "Subarray length must not exceed the length of the input array.\n"

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
        print(e + "\n")
        return

    try:
        while True:
            subarray_length = int(input("Enter the size of the subarray: "))

            if subarray_length > 0 and subarray_length <= len(array):
                break
            else:
                print("\nSubarray length must be a positive integer and less than or equal to the length of the main array.\n")
        
        assert subarray_length > 0, "Subarray length must be a positive integer."
        assert subarray_length <= len(array), "Subarray length must not exceed the length of the input array."
    except ValueError:
        print("Subarray length must be an integer.")
        return
    except AssertionError as e:
        print(e + "\n")
        return

    highest_average = find_highest_subarray_average(array, subarray_length)
    print(f"The highest average of a subarray of length {subarray_length} is: {highest_average}\n")

if __name__ == "__main__":
    main()

