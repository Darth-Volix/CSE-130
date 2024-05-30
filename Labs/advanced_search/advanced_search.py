# 1. Name:
#      Nicholas Wilkins
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Read a JSON file and perform an advanced search on a sorted array to find a target value.
# 4. Algorithmic Efficiency
#      The advanced search algorithm has a time complexity of O(log n) because it divides the array 
#      in half each time it compares the target value to the middle element. The start and end variables
#      are updated based on the compaison of the middle element to the target value, which means these
#      variables will always have a time complexity of 0(1). Howver, the while loop divides the array in
#      half with each iteration, which means that the number of iterations it takes to go from n elements
#      to 1 element is determeined by how many times you can divide n by 2 until you get to 1. This is
#      represented by the equation n / 2^x = 1, where x is the number of iterations. Solving for x gives
#      x = log n. This means the time complexity of the advanced search algorithm is O(log n).
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was understanding how to read a JSON file and extract the array from it. I had to
#      research how to read a JSON file and use the json module to extract the array from the file. Once I
#      understood how to do this, I was able to implement the json_reader function to read the JSON file 
#      properly. The rest of the program was pretty easy to do because I had already written pseudocode for
#      the advanced search algorithm and I have done lots of projects with python before. It also took some
#      time to figure out how to best explain the alogirthmic effiency of the advanced search algorithm, but
#      I was able to figure that out realtively quickly.
# 6. How long did it take for you to complete the assignment?
#      It took me about 2 hours to complete this assignment, which includes the time to write the program,
#      create the video demonstration, and complete the writeup.

import json

def advanced_search(array, target):
    '''
    Perform an advanced search on a sorted array to find a target value.

    Parameters:
        array (list): The sorted array to search in.
        target: The value to search for.

    Returns:
        bool: True if the target value is found in the array, False otherwise.
    '''
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return True
        
    return False

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

def main():
    try:
        # Prompt the user to enter the file name
        search_file = input("\nEnter the file name: ")
       
        # Read the JSON file
        array = json_reader(search_file)

        # Check if the array is not empty
        if len(array) > 0:

            # Prompt the user to enter the target
            target = input("Enter the target: ")

            # Check if the target is in the array
            if advanced_search(array, target):
                print(f"We found {target} in {search_file}.\n")
            else:
                print(f"{target} was not found in {search_file}.\n")
        else:
            print(f"{search_file} is empty.\n")

    # Handle exceptions
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()