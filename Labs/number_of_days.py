def is_leap_year(year):
    '''
    This function takes a year as input and returns True if the year is a leap year 
    and False otherwise.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    '''
    assert isinstance(year, int), "Year must be an integer"
    assert year >= 0, "Year must be non-negative"

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
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
    assert isinstance(month, int), "Month must be an integer"
    assert 1 <= month <= 12, "Month must be between 1 and 12"
    assert isinstance(year, int), "Year must be an integer"
    assert year >= 0, "Year must be non-negative"

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
    assert isinstance(start_date, tuple) and len(start_date) == 3, "Start date must be a tuple with three elements (day, month, year)"
    assert isinstance(end_date, tuple) and len(end_date) == 3, "End date must be a tuple with three elements (day, month, year)"

    # Break down the start and end dates into day, month, and year.
    start_day, start_month, start_year = start_date
    end_day, end_month, end_year = end_date

    assert isinstance(start_day, int) and 1 <= start_day <= days_in_month(start_month, start_year), "Invalid start day"
    assert isinstance(start_month, int) and 1 <= start_month <= 12, "Invalid start month"
    assert isinstance(start_year, int) and start_year >= 0, "Invalid start year"

    assert isinstance(end_day, int) and 1 <= end_day <= days_in_month(end_month, end_year), "Invalid end day"
    assert isinstance(end_month, int) and 1 <= end_month <= 12,  "Invalid end month"
    assert isinstance(end_year, int) and end_year >= 0 and start_year <= end_year, "Invalid end year"

    assert start_date != end_date, "Start and end dates cannot be the same"

    if start_year == end_year:
        assert start_month <= end_month, "Start month must be less than or equal to end month"
        
        if start_month == end_month:
            assert start_day < end_day, "Start day must be less than end day"
    
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
    
def main():

    # Get the start and end dates from the user.
    start_year = int(input("Start Year: "))
    start_month = int(input("Start Month: "))
    start_day = int(input("Start Day: "))
    end_year = int(input("End Year: "))
    end_month = int(input("End Month: "))
    end_day = int(input("End Day: "))

    # Format the dates for use in functions.
    start_date = (start_day, start_month, start_year)
    end_date = (end_day, end_month, end_year)

    # Calculate the number of days between the two dates.
    days = days_between_dates(start_date, end_date)

    # Display the result.
    print(f"\nThere are {days} days between the two dates.")

if __name__ == "__main__":
    main()