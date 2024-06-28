def is_leap_year(year):
    '''
    This function takes a year as input and returns True if the year is a leap year 
    and False otherwise.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    '''
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
    start_day, start_month, start_year = start_date
    end_day, end_month, end_year = end_date
    days = 0

    if start_year == end_year and start_month == end_month:
        days = end_day - start_day
        return days
    elif start_year == end_year:
        days += days_in_month(start_month, start_year) - start_day
        for month in range(start_month + 1, end_month):
            days += days_in_month(month, start_year)
        days += end_day
        return days
    else:
        days += days_in_month(start_month, start_year) - start_day
        for month in range(start_month + 1, 13):
            days += days_in_month(month, start_year)
        for year in range(start_year + 1, end_year):
            if is_leap_year(year):
                days += 366
            else:
                days += 365
        for month in range(1, end_month):
            days += days_in_month(month, end_year)
        days += end_day
        return days