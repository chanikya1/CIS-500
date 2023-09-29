#######################################################
# my_date
#
# Name: Chanikya Boggarapu (replace with your name)
# Section: 03
#
# Fall 2023
#########################################################

import datetime

def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year, False otherwise"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
 
def ordinal_date(year:int , month: int, day: int) -> int:
    """ Return the number of days elapsed since the beginning of the year, including any partial days.
        For example, the ordinal date for 1 January is 1.
        Hint: pre-compute the ordinal date for the first of each month."""
    first_of_month = datetime(year, month, 1)
    given_date = datetime(year, month, day)
    delta = given_date - first_of_month
    return delta.days + 1

def days_elapsed(year1: int, month1: int, day1: int, year2: int, month2: int, day2:int ) -> int:
    """ Return the number of days that have elapsed between year1-month1-day1 and year2-month2-day2.
        You may assume that year1-month1-day1 falls on or before year2-month2-day2. (In other words,
        your answer will always be >= 0.) """
    start_date = datetime(year1, month1, day1)
    end_date = datetime(year2, month2, day2)
    delta = end_date - start_date
    return delta.days

# This is a tuple. It is immutable so that users can't accidentally modify it.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day_of_week(year: int, month: int, day: int) -> str:
    """ Return the day of the week (Sunday, Monday, Tuesday, etc.) for the given day
        Hint 1: 1 January 1753 was a Monday.
        Hint 2: Use the methods you've already written."""
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    date = datetime(year, month, day)
    return weekdays[date.weekday()]
    
def to_str(year: int, month: int, day: int) -> str:
    """ Return this date as string of the form "Wednesday, 07 March 1833"."""
    date = datetime(year, month, day)
    formatted_date = date.strftime("%A, %d %B %Y")
    return formatted_date
              
    
def test_is_leap_year1(self):
	self.assertTrue(my_date.is_leap_year(1984))

def test_is_leap_year2(self):
    self.assertFalse(my_date.is_leap_year(1985))

    #
    # ordinal_date
    #

def test_ordinal_date1(self):
    self.assertEqual(1, my_date.ordinal_date(1997, 1, 1))

def test_ordinal_date2(self):
    self.assertEqual(32, my_date.ordinal_date(1995, 2, 1))

    #
    # days_elapsed  
    #

def test_days_elapsed1(self):
    self.assertEqual(1, my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))

def test_days_elapsed2(self):
    self.assertEqual(31, my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))

def test_days_elapsed3(self):
    self.assertEqual(365, my_date.days_elapsed(1997, 1, 1, 1998, 1, 1))

    # Warning: You need more tests than you think for this function

    #
    # day_of_week
    #

def test_day_of_week1(self):
    self.assertEqual("Monday", my_date.day_of_week(1753, 1, 1))


    #
    # to_str
    #
def test_to_str1(self):
	self.assertEqual("Wednesday, 02 August 2024", my_date.to_str(2024, 8, 2))