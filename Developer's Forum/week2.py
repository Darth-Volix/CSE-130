
def days_in_month(month, year):
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_per_month[month]

def days_between_dates(start_date, end_date):
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
            days += 366 if is_leap_year(year) else 365
        for month in range(1, end_month):
            days += days_in_month(month, end_year)
        days += end_day
        return days