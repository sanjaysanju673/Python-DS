'''
@Author: v sanjay kumar
@Date: 2024-07-22 10:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 10:30:30
@Title : Calculate Number of Days Between Two Dates
'''

from datetime import date

def calculate_days_between_dates(date1, date2):
    '''Calculates the number of days between two dates.

    Parameters:
    date1 (tuple): The first date as a tuple in the format (year, month, day).
    date2 (tuple): The second date as a tuple in the format (year, month, day).

    Returns:
    int: The number of days between the two dates.
    '''
    d1 = date(date1[0], date1[1], date1[2])
    d2 = date(date2[0], date2[1], date2[2])
    delta = d2 - d1
    return delta.days

def main():
    try:
        year1 = int(input("Enter the year of the first date: "))
        month1 = int(input("Enter the month of the first date: "))
        day1 = int(input("Enter the day of the first date: "))
        date1 = (year1, month1, day1)

        year2 = int(input("Enter the year of the second date: "))
        month2 = int(input("Enter the month of the second date: "))
        day2 = int(input("Enter the day of the second date: "))
        date2 = (year2, month2, day2)

        days_between = calculate_days_between_dates(date1, date2)
        print(f"Number of days between {date1} and {date2} is {days_between} days")

    except ValueError:
        print("Invalid input. Please enter numeric values for year, month, and day.")

if __name__ == "__main__":
    main()



