import json

def json_reader(file_name):
    '''
    Read a JSON file and return the array.

    Parameters:
        file_name (str): The name of the JSON file.

    Returns:
        array: The array read from the JSON file.
    '''
    with open(file_name, 'r') as file:
        data = json.load(file)

    array = data['array']

    return array

def sort_algorithm(array):
    '''
    Takes an unsorted array and assorts it.

    Parameters:
        array (list): The unsorted array.

    Returns:
        list: The sorted array.
    '''
    array_length = len(array)
    for i in range(array_length - 1, 0, -1):
        largest_element = 0
        for j in range(1, i + 1):
            if array[j] > array[largest_element]:
                largest_element = j
        array[largest_element], array[i] = array[i], array[largest_element]

    return array

def main():
    try:
        # Prompt the user to enter the file name
        search_file = input("\nEnter the file name: ")
       
        # Read the JSON file
        array = json_reader(search_file)

        # Check if the array is not empty
        if len(array) > 0:
            
            # Sort the array
            sorted_array = sort_algorithm(array)
            
            # Print the sorted array
            print(f"\nSorted array: {sorted_array}\n")

        else:
            print(f"{search_file} is empty.\n")

    # Handle exceptions
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()