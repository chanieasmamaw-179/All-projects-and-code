
Exercise 1 · Print age
Complete the function age.
The function expects one parameter (argument) called year (int).
The function will return the following string (in this example. when year is 1983):
You were born in 1983, so you are about 40 years old.
Hint: Don’t use print inside the function.
Exercise 2 · Sum
Define a function named my_sum that accepts 2 numbers (int).
The function should sum all the numbers and return the result
Exercise 3 · Concat
Define a function named special_concat that accepts 3 strings (str).
The function should concat all the strings and return the result in the following format (str):
>> print(special_concat(”Cats”, “Dogs”, “Wolfs”)) Cats, Dogs & Wolfs
Exercise 4 · Currency Convertor
Write a function called usd_to_yuan, that will get one parameter - An amount of money in US Dollars (int)
The function will convert the amount to the equivalent amount in Chinese Yuan, and return the result (float).

Exercise 5 · Title Creator
Write a function called title_creator.
The function will expect three parameters:
title (str) - the text for the title.
char (str) - the character surrounding the text.
times (int) - the number of times to repeat the character on each side of the title.
The function will return a formatted title (str), as shown in the example.
Exercise 6 · Coffee Cost
You're ordering coffee for your office. A small coffee costs $2, a medium coffee costs $3, and a large coffee costs $4.
Write a function coffee_calculator that takes three parameters - the number of each size coffee (ints), and returns the total cost of the order (int).
Exercise 7 · Percent calculation
Write a function called percent. This function will calculate the percentage of one number relative to another.
The function will accept two parameters: num1 (int) and num2 (int).
The function will return the calculated percentage as a string, like 25.5%.
Exercise 8 · Price with Tax
In a certain country, tax is only applied to the portion of an item's cost that exceeds 100$. The tax rate is 25%.
Write a function called add_tax.
The function will expect one parameter - price (int) - the price of an item in dollars. You can assume the price is larger than 100$.
The function will return the full price, including taxes (float).
Exercise 9 · Distance between points
Create a function named euclidean_distance that receives 4 floats: x1, y1, x2, y2
The function should calculate and return the euclidean distance between the point (x1, y1) to (x2, y2)
The euclidean distance formula is the following:
=(1−2)2+(1−2)2Distance=(x1−x2)2+(y1−y2)2​

Exercise 10 · Middle digit
Write a function called middle_digit.
The function will expect one parameter called num, which is a 3-digit number (int).
The function will return the middle digit of the number (int).
BONUS Exercise 11 · Reverse numbers
Write a function called reverse_number that takes a five-digit number as input (int) and returns the number in reverse order (int). For example, reverse_number(12345) would return 54321.








###################### EX......1 ###################
def age(year) -> str:
    current_year = 2023
    calculated_age = current_year - year
    return f"You were born in {year}, so you are about {calculated_age} years old."

# Example usage:
year_of_birth = 1983
calculated = age(year_of_birth)
print(calculated)

###################### EX......2 ###################
def my_sum(a,b):
    c=a+b
    print(c)
    return c
my_sum(1, 2)
###################### EX......3 ###################

def special_concat(str1, str2, str3):
    concat_string = str1 + ", " + str2 + " & " + str3
    return concat_string
print(special_concat("Cat", "Dog", "Wolfs"))
###################### EX......4 ###################

def usd_to_yuan (USD):
    exchange_rate = float(7.15)
    US_Dollar_USD = exchange_rate * USD
    print(US_Dollar_USD)
    return US_Dollar_USD
usd_to_yuan(10)
###################### EX......5 ###################
def title_creator(title, chara, times):
    return chara * times + title + chara * times

print(title_creator("Welcome to Masterschool", "=", 5))

###################### EX......6 ###################
def coffee_calculator(small, medium, large):
    Total_cost = small*2 + medium*3 + large*4
    print("Total cost in $:",Total_cost)
    return Total_cost
coffee_calculator(2,10,1)
###################### EX......7 ###################
def percent(num1: int, num2: int) -> str:
    if num2 == 0:
        return "Undefined"
    percentage = (num1 / num2) * 100
    print(percentage)
    return f"{percentage:.1f}%"
percent(250,125)
###################### EX......8 ###################
def add_tax(price: float, tax_rate: float = 25.0) -> float:
    if price <= 100:
        return price
    else:
        taxable_amount = price - 100
        tax = taxable_amount * (tax_rate / 100)
        total_amount = price + tax
        print(total_amount)
        return total_amount
add_tax(120)
###################### EX......9 ###################
import math
def euclidean_distance(x1, y1, x2, y2):
    Distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("Distance is:", Distance)
    return Distance
euclidean_distance(0, 0, 3, 4)

###################### EX......10 ###################
def middle_digit(number: int) -> int:
    # Convert the number to a string to access individual digits
    num_str = str(number)
    length = len(num_str)

    if length % 2 == 1:
        middle_index = length // 2
        return int(num_str[middle_index])
    else:
        return None
result = middle_digit(902)
if result is not None:
    print(result)
###################### EX......11 ###################
def reverse_number(number: int) -> int:
    reversed_str = str(number)[::-1]
    reversed_number = int(reversed_str)
    print(reversed_number)
    return reversed_number
result = reverse_number(23345)