#Given your birthday, in the format "DD-MM-YYYY", write a function that calculates
# how many days have passed since your birthday (without counting the days in your
# birth year and the current year, so just whole years).
#the function takes your birthday as a parameter in string format.



def days_passed_since_birthday(birthday):
    # first, we must split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # then, we must define the number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # initialize a variable to count the days
    days_passed = 0

    # calculate days passed in whole years
    for y in range(year + 1, 2024):  # Assuming 2024 is the current year
        # Check if the year is a leap year
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            days_passed += 366  # Leap year has 366 days
        else:
            days_passed += 365  # Non-leap year has 365 days

    # Subtract days in the birth year
    for m in range(month - 1):
        days_passed -= days_in_month[m]
    days_passed -= (day - 1)  # Subtract days passed in the birth month

    return days_passed

# Test the function
birthday = "21-06-2004"
days_passed = days_passed_since_birthday(birthday)
print("Days passed since birthday (excluding birth year and current year):", days_passed)
