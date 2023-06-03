def leap_year(year):
    """Given a year, report if it's a Leap one."""
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
