
##### Exercise 1 ###############
def Now_age(year):
    curruent_year = int(2023)
    Age_now= curruent_year - year
    print(Age_now)
    return Age_now
Now_age(1983)
##### Exercise 2 ###############
def my_sum(a,b):
    c=a+b
    print(c)
    return c
my_sum(1, 2)
##### Exercise 3###############
def special_concat():
    name1 = "Cats"
    name2 = "Dogs"
    name3 = "Wolfs"
    concate_Name = name1+","+ name2 + ","+name3
    print (concate_Name)
    return concate_Name
special_concat()
##### Exercise 4###############

def usd_to_yuan (USD):
    exchange_rate = float(7.15)
    US_Dollar_USD = exchange_rate * USD
    print(US_Dollar_USD)
    return US_Dollar_USD
usd_to_yuan(10)

##### Exercise 5###############
def title_creator():
    welcome_message = "="*5 + "Welcome to Masterschool" + "=" * 5
    print(welcome_message)
title_creator()
##### Exercise 6 ###############

def coffee_calculator(small_coffe ,medium_coffe ,large_coffe  ):
    total_cost = small_coffe + medium_coffe + large_coffe
    print("Total cost is:", total_cost,"$")
    return total_cost

coffee_calculator(2,10,1)


##### Exercise 7###############
def percent(num1, num2):
    percent = (num1/num2)*100
    print(percent,"%")
    return percent
percent(250,125)
####### Exercise 8 ########
def add_tax(tax):
    price_before_tax=100 # (in $)
    Sales_tax = (tax )* price_before_tax # 7.25 sales tax in percent
    Total_price_with_tax = price_before_tax + Sales_tax
    print("Total Price with tax:$", Total_price_with_tax,)
    return Total_price_with_tax
add_tax(0.11)

#######Exercise 9 ######
import math
def euclidean_distance(x1, y1, x2, y2):
    Distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("Distance is:", Distance, "km")
    return Distance
euclidean_distance(0, 0, 3.0, 4.0)
#######Exercise 10 ######
def middle_digit(num):
    if 200 <= num <= 666:
        num_str = str(num)
        middle_digits = num_str[1]
        print(f" the midil digit is:",middle_digits)
    else:
        print("Please provide a valid three-digit number.")
middle_digit(303)
#######Exercise 11 ######
def reverse_number(number):
  number=format(int(number))
  reversed_number=number[::-1]
  print(f"Reverse number is: ",reversed_number)
  return reversed_number
reverse_number(45369)












