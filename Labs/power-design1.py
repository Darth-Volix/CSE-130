


def find_max_average(numbers, j):
    '''
    This function finds the maximum average of a subarray of length j in a given array.

    Parameters:
        numbers (list): The input array.
        j (int): The length of the subarray.

    Returns:
        float: The maximum average of a subarray of length j.
    '''
    # Initialize the highest average
    highest_average = 0

    # Iterate through the array
    i = 0
    while i + (j - 1) < len(numbers):
        # Get the subarray
        subarray = numbers[i:i + j]

        # Calculate the average of the subarray
        average = sum(subarray) / j

        # Update the highest average if necessary
        if average > highest_average:
            highest_average = average

        i += 1

    return highest_average

def main():
    # Test the function
    numbers = [1, 12, -5, -6, 50, 3]
    j = 4
    print(find_max_average(numbers, j))  # Output: 12.75

if __name__ == "__main__":
    main()

