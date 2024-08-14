


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Q1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
1. With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.

"""
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Q2 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
2. Fill in the left side of line 7 so that the following code runs without error
"""

def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

area = circle_info(10)
print("area is " + str(area))
print("circumference is " + str(circle_info))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Q3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
3. Define a function called date_split that receives one parameter: a date string in the format “DD-MM-YYYY”
(f.e. “24-05-1986”). The function should then return a tuple with 3 elements - day, month, year, all as strings.

"""
"""
def date_split(inputs: str) -> tuple:
    para_split = inputs.split("-")  # Splitting by hyphen
    day, month, year = para_split   # Unpacking into day, month, year
    return day, month, year         # Returning as a tuple

parameter = input("Enter date (day-month-year): ")
result = date_split(parameter)
print("Date components:", result)
"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Q4 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
4. Update the function date_split from previous exercise, so it returns all values as ints.
"""


def date_split(inputs: str) -> tuple:
    para_split = inputs.split("-")  # Splitting by hyphen
    day, month, year = para_split   # Unpacking into day, month, year
    return int(day), int(month), int(year)  # Returning as integers in a tuple

parameter = input("Enter date (day-month-year): ")
day, month, year = date_split(parameter)
print("Date components:", day, month, year)
















