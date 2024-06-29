# 1. Name:
#      Nicholas Wilkins
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program calculates the number of days between two dates.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was making sure that I had assert statements
#      for all possible cases. I had to make sure that the start and end dates were valid,
#      that the start date was not equal to the end date, and that the start date was less
#      than the end date. I also had to make sure that the start date was less than or equal
#      to the end date if they were in the same month. Troubleshooting those assert statements
#      to make sure they were consistent with the logic of the program was the next hardest part.
# 5. How long did it take for you to complete the assignment?
#      This assignment took me about 2 hours to complete. 1.5 hours to write the code and 30 minutes
#      to film the video and submit it.

def is_leap_year(year):
    '''
    This function takes a year as input and returns True if the year is a leap year 
    and False otherwise.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    '''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def days_in_month(month, year):
    '''
    This function takes a month and a year as input and returns the number of days in 
    that month.

    Parameters:
        month (int): The month to check.
        year (int): The year to check.

    Returns:
        int: The number of days in the month.
    '''
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29
    
    return days_per_month[month]

def days_between_dates(start_date, end_date):
    '''
    This function takes two dates as input and returns the number of days between them.

    Parameters:
        start_date (tuple): The start date in the format (day, month, year).
        end_date (tuple): The end date in the format (day, month, year).

    Returns:
        int: The number of days between the two dates.
    '''
    # Break down the start and end dates into day, month, and year.
    start_day, start_month, start_year = start_date
    end_day, end_month, end_year = end_date

    assert start_year <= end_year, "End year must be greater than or equal to start year"
    assert start_date != end_date, "Start and end dates cannot be the same"

    if start_year == end_year:
        assert start_month <= end_month, "End month must be greater than or equal to start month"
        
        if start_month == end_month:
            assert start_day < end_day, "End day must be greater than start day"
    
    days = 0

    # Check if the start and end dates are in the same year and month.
    if start_year == end_year and start_month == end_month:
        days = end_day - start_day
        
        return days
    
    # Check if the start and end dates are in the same year but different months.
    elif start_year == end_year:

        # Add days for the remaining days in the start month.
        days += days_in_month(start_month, start_year) - start_day

        # Add days for the months between the start and end months.
        for month in range(start_month + 1, end_month):
            days += days_in_month(month, start_year)

        # Add days for the end month.
        days += end_day
        
        return days
    
    # If the start and end dates are in different years.
    else:

        # Add days for the remaining days in the start month.
        days += days_in_month(start_month, start_year) - start_day

        # Add days for the remaining months in the start year.
        for month in range(start_month + 1, 13):
            days += days_in_month(month, start_year)

        # Add days for the full years between the start and end years.
        for year in range(start_year + 1, end_year):
            if is_leap_year(year):
                days += 366
            else:
                days += 365

        # Add days for the months in the end year.
        for month in range(1, end_month):
            days += days_in_month(month, end_year)

        # Add days for the end month.
        days += end_day

        return days
    
def get_valid_date(prompt):
    '''
    This function prompts the user to enter a valid date and returns it as a tuple.

    Parameters:
        prompt (str): The prompt message to display to the user.

    Returns:
        tuple: The valid date entered by the user in the format (day, month, year).
    '''
    while True:
        try:
            year = int(input(f"{prompt} Year: "))
            assert isinstance(year, int), "Year must be an integer"
            assert year >= 1753, "Year must be 1753 or later"
            
            month = int(input(f"{prompt} Month: "))
            assert isinstance(month, int), "Month must be an integer"
            assert 1 <= month <= 12, "Month must be between 1 and 12"
            
            day = int(input(f"{prompt} Day: "))
            assert isinstance(day, int), "Day must be an integer"
            assert 1 <= day <= days_in_month(month, year), "Invalid day for the given month and year"
            
            return (day, month, year)
        
        except (ValueError, AssertionError) as e:
            print(f"\nInvalid input: {e}. Please try again.\n")

def main():
    while True:
        try:
            start_date = get_valid_date("Start")
            end_date = get_valid_date("End")
            days = days_between_dates(start_date, end_date)

            print(f"\nThere are {days} days between the two dates.")
            break

        except (ValueError, AssertionError) as e:
            print(f"\nIvalid Input: {e}. Please try again.\n")

if __name__ == "__main__":
    main()