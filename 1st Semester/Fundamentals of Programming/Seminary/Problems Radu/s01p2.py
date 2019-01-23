'''

@author: radu

2. Compute the age of a person in number of days. So, given the date of birth 
of a person in the format dd mm yyyy (three integers) and the current date
(in the same format) compute the age of that person in number of days. 

'''

def leap(year):
    """Check if a year is leap.
    
    Given a year in the format yyyy, check if it is a leap year.
    
    Arguments:
        year - integer (yyyy).
    Returns:
        True if year is leap or False otherwise. 
    """
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def days(month):
    """Returns the number of days in a month.
    
    Given a month (integer - mm) return the number of days 
    in that month (without considering leap years).
    
    Arguments:
        month - integer (mm).
    Returns:
        The number of days in month.
    """
    if month == 2:
        return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

def compute_position(d, m, y):
    """Computes the position of a date in a year.
    
    Given a date (dd mm yyyy - three integers), compute the position of that 
    date in the given year, i.e., how many days have passed from the beginning
    of the year to the given date.
    
    Arguments:
        d,m,y - integers; a date in the format (dd, mm, yyyy).
    Returns:
        the number of days that have passed from the beginning of year y 
        to the date given by d, m, y.  
    """
    p = 1 if leap(y) and m > 2 else 0
    for i in range (1, m):
        p += days(i)
    return p + d

def compute_age(d1, m1, y1, d2, m2, y2):
    """Returns the age of a person in number of days.
    
    Given the date of birth 
    of a person in the format dd mm yyyy (three integers) and the current date
    (in the same format) compute the age of that person in number of days.
    
    Arguments:
        d1,m1,y1 - integers denoting the date of birth (dd mm yyyy)
        d2,m2,y2 - integers denoting the current date (dd mm yyyy)        
    Returns:
        The age of a person in number of days.
    """
    age = compute_position(d2, m2, y2)
    for i in range(y1, y2):
        age += 365
        if leap(i):
            age += 1
    return age - compute_position(d1, m1, y1)   

if __name__ == '__main__':
    print(compute_age(1, 3, 2000, 1, 1, 2010))
