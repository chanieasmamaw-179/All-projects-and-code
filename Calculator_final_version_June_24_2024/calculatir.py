import math

basic_operators_options = ("+", "-", "*", "/", "~")
advanced_operations = ("sin", "cos", "tan", "pi", "e", "sqrt")


def get_operator(operation):
	for element in basic_operators_options:
		if element in operation:
			return element
	for element in advanced_operations:
		if element in operation:
			return element
	return None


def calculate(operation):
	operator = get_operator(operation)
	if operator in basic_operators_options:
		operands = operation.split(operator)
		if len(operands) != 2:
			print("Invalid operation format. Ensure the operation is in the form 'num1 operator num2'.")
			return
		
		try:
			num1 = int(operands[0])
			num2 = int(operands[1])
		except ValueError:
			print("Invalid numbers. Please enter valid numerical values.")
			return
		
		if operator == "+":
			print(f"The answer is: {num1 + num2}")
		elif operator == "-":
			print(f"The answer is: {num1 - num2}")
		elif operator == "*":
			print(f"The answer is: {num1 * num2}")
		elif operator == "/":
			if num2 != 0:
				print(f"The answer is: {num1 / num2}")
			else:
				print("Error: Division by zero is not allowed.")
		elif operator == "~":
			if num2 != 0:
				print(f"The  answer is: {num1 // num2}")
				print(f"The answer is: {num1 % num2}")
			else:
				print("Error: Division by zero is not allowed.")
	elif operator in advanced_operations:
		if operator == "pi":
			print(f"Value of pi is {math.pi}")
		elif operator == "e":
			print(f"Value of e is {math.e}")
		else:
			operand = operation.replace(operator, "").strip("()")
			try:
				num = float(operand)
			except ValueError:
				print("Invalid number. Please enter a valid numerical value.")
				return
			
			if operator == "sin":
				print(f"The answer is: {math.sin(math.radians(num))}")
			elif operator == "cos":
				print(f"The answer is: {math.cos(math.radians(num))}")
			elif operator == "tan":
				print(f"The answer is: {math.tan(math.radians(num))}")
			elif operator == "sqrt":
				if num >= 0:
					print(f"The answer is:  {math.sqrt(num)}")
				else:
					print("Error: Square root of a negative number is not allowed.")
	else:
		print("Invalid operation. Please choose a valid operator or function.")


def perform_calculations():
	try:
		num_calculations = int(input("How many calculations do you want to perform? "))
	except ValueError:
		print("Invalid input. Please enter an integer.")
		return
	
	for num in range(num_calculations):
		operation = input("What do you want to calculate: ").strip()
		calculate(operation)

print("Welcome to the Python calculator!")
perform_calculations()
