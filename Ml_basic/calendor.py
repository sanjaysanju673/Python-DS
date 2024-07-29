'''
@Author: v sanjay kumar
@Date: 2024-07-22 10:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-22 10:30:30
@Title : Print Calendar for Given Month and Year
'''

import calendar

def print_month_calendar(year, month):
    '''Prints the calendar for a given month and year.

    Parameters:
    year (int): The year for which the calendar is to be printed.
    month (int): The month for which the calendar is to be printed.

    Returns:
    None
    '''
    try:
        cal = calendar.month(year, month)
        print(cal)
    except IndexError:
        print("Invalid month. Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid year. Please enter a valid year.")

def main():
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        print_month_calendar(year, month)
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")

if __name__ == "__main__":
    main()
