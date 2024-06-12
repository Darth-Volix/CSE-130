# 1. Name:
#      Nicholas Wilkins
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program reads a JSON file containing an array of strings, sorts the array 
#      using a sorting algorithm, and prints the sorted array.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was not the algorithm itself, but the part
#      where I had to add some assertions to ensure that the program was working correctly.
#      As a programmer, I am used to writing code that I know works, so trying to think
#      of all the possible ways that the program could fail was a bit challenging and 
#      required some study of my code and thinking in order to determine the possible 
#      places in the code where the program could fail if the input or logic was incorrect.
# 5. How long did it take for you to complete the assignment?
#      It took me about 2.25 hours to complete this assignment, with 10 minutes of that time
#      spent on reading the assignment instructions and requirements, 1 hour and 30 minutes
#      spent on writing the code, and 20 minutes spent on testing the code and writing the
#      assertion statements. The last 15 minutes was spent making the video.

import json

def json_reader(file_name):
    '''
    Read a JSON file and return the array.

    Parameters:
        file_name (str): The name of the JSON file.

    Returns:
        array: The array read from the JSON file.
    '''
    # Open the file and load the content
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    # Set the variable "array" to the value of the key "array" in the JSON file
    array = data['array']

    # Ensure that the data in "array" is a list
    assert isinstance(array, list), "The data read from the file should be a list."

    return array

def sort_algorithm(array):
    '''
    Takes an unsorted array and sorts it using the selection sort algorithm.

    Parameters:
        array (list): The unsorted array.

    Returns:
        list: The sorted array.
    '''
    # Ensure the input is a list
    assert isinstance(array, list), "Input should be a list."

    # Get the length of the array
    array_length = len(array)
    
    # Perform the sort
    for i in range(array_length - 1, 0, -1):
        largest_element = 0
        for j in range(1, i + 1):
            if array[j] > array[largest_element]:
                largest_element = j

        # Ensure indices are within correct range before swapping
        assert largest_element < array_length, "Index out of range for swapping."
        assert i < array_length, "Index out of range for swapping."
        
        # Swap the largest element with the element at index i
        array[largest_element], array[i] = array[i], array[largest_element]
    
    # Ensure the array is correctly sorted
    assert array == sorted(array), "The array is not sorted correctly."

    return array

def main():
    try:
        # Prompt the user to enter the file name
        unsorted_file = input("\nEnter the file name: ")
       
        # Read the JSON file
        array = json_reader(unsorted_file)

        # Check if the array is not empty
        if len(array) > 0:
            
            # Sort the array
            sorted_array = sort_algorithm(array)
            
            # Print the sorted array
            print(f"The values in {unsorted_file} are:")
            for value in sorted_array:
                print("         "+ value)
            print("")

        else:
            print(f"{unsorted_file} is empty.\n")

    # Handle any exceptions
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()