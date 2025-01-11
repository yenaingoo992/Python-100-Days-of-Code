# functions that can output the result
def format_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"

print(format_name("ye", "naing"))


def is_leap_year(year):
    """receiving year as input, then decide and return if that year is leap year or not."""
    is_leap_year = False
    if year % 4 == 0:
        is_leap_year = True
    if year % 100 == 0 and year % 400 != 0:
        is_leap_year = False
    
    return is_leap_year

print(is_leap_year(1700))