#########################################  Qestion 1 ###################################################################
#def questions()
"""
    Write a function called extract_area_code.
The function will expect one parameter: phone_number, a string containing a phone number in the format “(XXX) YYY-ZZZZ".
The function will return a new string containing the extracted area code.
    :return:
"""
def extract_area_code(phone_number):
    # Check  format (like (XXX) YYY-ZZZZ)
    if phone_number.startswith("(") and ")" in phone_number:
        start_index = phone_number.index("(") + 1
        end_index = phone_number.index(")")
        area_code = phone_number[start_index:end_index]
        return area_code
    else:
        return "Invalid input"

result = extract_area_code("(120)-176-253-15666")
print(result)  # Should print (xxx)

#########################################  Qestion 2 ###################################################################
"""
Write a function called duplicate_last_item. The function will expect one parameter: a list with unknown elements.
The function will add a copy of the last item to the end of the list, and return the updated list.
"""
def duplicate_last_item(list_item):
    if not list_item:
        return list_item
    list_item.append(list_item[-1])
    return list_item
result = duplicate_last_item(["A", 2, "A", "B", "C", "D", "E", "F", "G", "H"])
print(result)
#########################################  Qestion 3 ###################################################################

"""
In a certain country, only items that cost more than $100 are taxed. The tax rate is 15%.
Write a function called add_tax. 
The function will expect one parameter - price (float) - the price of an item in dollars.
The function will return the full price, including taxes, if applied (float).
"""
tax_free_threshold = 100
tax_rate=0.15
def add_tax(price) -> float:
    price = float(price)  # Convert price to float
    if price < tax_free_threshold:
        return price  # Tax-free
    else:
        return price + (price * tax_rate)

# Ensure both arguments are provided
result = add_tax(120)
print(f"The final price after tax is: {result:.2f} $")

# Another example with a price below the threshold
result2 = add_tax(10)
print(f"The final price after tax is: {result2:.2f} $")

#########################################  Qestion 4 ###################################################################
"""
Write a function called count_first_letter.
The function will expect one parameter: text, a string containing the text to analyze.
The function will return the number of times the first letter appears in the text (int).
"""
def count_first_letter(text: str) -> int:
    if not text:
        return 0
    first_letter = text[0].lower()
    count = text.lower().count(first_letter)
    return count
# Example usage
result = count_first_letter('Asmamaw')
print(result)
#########################################  Qestion 5 ###################################################################
"""
After moving from Europe to the US, Jane found herself constantly struggling with date formats. She decided to write a simple program to automatically reformat her calendar's American-formatted dates into the more familiar European style.
Write a function called reformat_date. The function will expect one parameter: date, a string in the format MM-DD-YYYY.
The function will return the same date as a string in the format of DD/MM/YYYY.
"""
def reformat_date(birth_date):
    # Split the input date by "/"
    date_parts = birth_date.split("-")
    if len(date_parts) != 3:
        return "Invalid date format. Please enter the date in dd/mm/yyyy format."
    day, month, year = date_parts

    # Return the reformatted date as "yyyy-mm-dd"
    reformatted_date = f"{month}-{day}-{year}" and f"{month}/{day}/{year}"
    return reformatted_date

result = reformat_date("02-06-2024")
print(result)
#########################################  Qestion 6 ###################################################################

"""
Exercise 6 - Generate Case Variants
A digital advertising platform needs to create variations of headlines in both uppercase and lowercase.
Write a function called generate_case_variants, that will expect one parameter: text, a string that needs to be converted.
The function will return a list containing the lowercase and then the uppercase version of the text.
"""
def generate_case_variants(text):
    text = text.lower()
    text_upper=text.upper()
    concatinet_text =  [text ,  text_upper]
    return concatinet_text
result=generate_case_variants(("Asmamaw Chanie") )
print(result)
#########################################  Qestion 7 ###################################################################
"""
Exercise 7 - Summer Discount
A supermarket has started to offer a special summer discount. To qualify for this discount, a shopping list must contain at least 5 items, and one of them must be “Ice Cream”.
Write a function called validate_discount that will expect one parameter: a list of strings products.
If the shopping list qualifies for the discount, return "YES"; otherwise, return "NO".
"""
def validate_discount(products) -> str:
    if len(products) >= 5 and "Ice Cream" in products:
        return "YES"
    else:
        return "NO"
# Test the function
result = validate_discount(["Ice Cream", "Banana"])
print(result)  # Should print "Yes"

#########################################  Qestion 8 ###################################################################
"""
Exercise 8 - Pass or Fail
As part of a university course, students were required to take two exams. 
To successfully complete the course, students needed to fulfill two conditions: 
Their average grade must be 75 or higher
They must not receive a failing grade (55 or lower) on either exam.
Write a function called has_passed. 
The function will expect two parameters called grade1 and grade2 (ints).
The function will return a string “PASS” or “FAIL” according to the above conditions.
"""
def has_passed(grade_1: int, grade_2: int) -> str:
    if (grade_1 + grade_2) / 2 >= 75 and grade_1 >= 55 and grade_2 >= 55:
        return "PASS"
    else:
        return "FAIL"
result = has_passed(100, 45)
print(result)
#########################################  Qestion 9 ###################################################################
"""
Exercise 9 - Sentence, Period.
The editor of a local newspaper has a recurring problem - the reporters hand in articles and forget to add a period at the end of the sentences.
Write a function called period_adder.  The function will expect one parameter called sentence which holds a single sentence (str).
The function will return the sentence (str) with a single period at the end, regardless of whether there was a period there in the first place.
The only exception is sentences that end with a “!”, in which case there is no need to add a period.
"""
def period_adder(sentence: str) -> str:
    if sentence.endswith("!"):
        return sentence
    else:
        return sentence + "."
result = period_adder("What a lovely day!")
print(result)
#########################################  Qestion 10###################################################################
"""
Exercise 10 - Currency Converter Pro
Let’s create a currency converter that can handle two directions of conversion: EUR (€) to USD ($) and vice versa.
Write a function called convert that will receive a string like "$120" or "€50”, perform the conversion, and return it as a string with the other currency symbol.
Use the following conversion rates:
1 EUR = 1.10 USD
You may assume that the input to the convert function will be a whole number.
The returned price string should be up to 2 digits, you can do that using
      round(float_number, 2)
"""
def convert(amount) -> str:
    if amount.startswith("€"):
        converted_amount = float(amount[1:]) * 1.10
        return f"${round(converted_amount, 2)}"
    elif amount.startswith("$"):
        converted_amount = float(amount[1:]) / 1.10
        return f"€{round(converted_amount, 2)}"
    else:
        return "Invalid input"
result1 = convert("$110")
print(result1)  # Should print the converted amount in EUR
result2 = convert("€50")
print(result2)  # Should print the converted amount in USD

#########################################  Qestion 11 ###################################################################
"""
 Exercise 11 - Leap year
A leap year is a special year that contains an additional day. It’s used to keep our calendar in alignment with the Earth's revolutions around the Sun. It takes the Earth about 365.24 days to complete one full orbit around the Sun. As a result, if we didn't add a leap day approximately every 4 years, our calendar would slowly drift out of sync with the Earth's revolutions.
Determining which years are leap years involves a few rules:
The year must be evenly divisible by 4.
Unless it’s also a century year (like 1900, 2000, etc.), and then it must also be divisible by 400 to be considered a leap year.
Write a function is_leap that takes a year as input (int) and checks whether it's a leap year or not. 
If it is a leap year, return "Leap year" (str). If it's not a leap year, return "Not a leap year" (str). 
"""
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "Leap year"
    else:
        return "Not a leap year"
result1 = is_leap(2020)
result2 = is_leap(2021)
print(result1)  # Should print True
print(result2)  # Should print False
######################## Congratulations!! You passed the exam spring Assement Score 110/100!!!########################