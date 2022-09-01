def deadline_validator(deadline):
    deadline_split = deadline.split("/")
    day = int(deadline_split[0])
    month = int(deadline_split[1])
    year = int(deadline_split[2])
    
    if (day < 1 or day > 31):
        return False
    
    if (month < 1 or month > 12):
        return False
    
    month_to_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    
    if (is_leap_year):
        month_to_days[1] = 29
    
    if (day > month_to_days[month - 1]):
        return False
    
    return True