
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def determine_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400== 0)

def calculate_days():
    current_day = 1
    sundays = 0
    for i in range(2000-1900):
        for day in days_in_month:
            current_day += day
            if day == 28:
                current_day += determine_leap(i)
            if current_day % 7 == 0:
                sundays += 1
    return sundays

print("Number of sundays: {}".format(calculate_days()))
