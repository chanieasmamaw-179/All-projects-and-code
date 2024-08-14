import math
from datetime import date
################ This Project is written by Dr.Asmamaw Yehun (PhD), software Engineering/Software Developer#############
# at Masterschool, Berlin: chanieasmamaw@yahoo.com , Whatsapp +4917625315666 ##########################################
# Get the current date
current_date = date.today()
print("Current date:", current_date)


def welcome_message(name):
	message = f"""
    #**************************************+++++++++++++++++++++++++++++++++++#
    *     Welcome to Python Multiple Calculator                               *
    +     {name}                                                              +
    *     Thank you for joining us. Masterschool, Software Engineering, 2024  +
    *     Asmamaw Yehun (PhD, current: software Engineer/software Developer   +
    +     chanieasmamaw@yahoo.com                                             +
    +     Nitzan (Famile Name?)                                               +
    +     software Engineer/software Developer                                +
    *     nitzan@faculty.masterschool.com                                     *
    #**************************************+++++++++++++++++++++++++++++++++++#
    """
	print(message)


# Get user input
user_name = "This is one of power of python application"
welcome_message(user_name)

print("Welcome to the Python calculator!")


def custom_operation(a, b):
	quotient, remainder = divmod(a, b)
	return quotient, remainder


def perform_calculations():
	while True:
		# Ask the user for the number of calculations
		try:
			num_calculations = int(input("How many calculations do you want to perform? "))
		except ValueError:
			print("Invalid input. Please enter an integer.")
			continue
		
		# Ask the user for the type of calculation
		operation = input(
			"Choose an operation (add, subtract, multiply, divide) or type 'advanced' for advanced operations, 'exit' to quit: ").strip().lower()
		
		# Check if the user wants to exit
		if operation == 'exit':
			print("Exiting the program. Goodbye © Masterschool, Owner of Software Engineering Section, 2024!")
			break
		
		# Handle advanced operations
		if operation == 'advanced':
			advanced_calculate()
			continue
		
		# Perform the calculations
		for _ in range(num_calculations):
			# Request the operands
			try:
				num1 = float(input("Enter the first number: "))
				num2 = float(input("Enter the second number: "))
			except ValueError:
				print("Invalid input. Please enter numbers.")
				continue
			
			# Perform the chosen operation
			if operation == "add":
				result = num1 + num2
				print(f"The result of {num1} + {num2} is {result}")
			elif operation == "subtract":
				result = num1 - num2
				print(f"The result of {num1} - {num2} is {result}")
			elif operation == "multiply":
				result = num1 * num2
				print(f"The result of {num1} * {num2} is {result}")
			elif operation == "divide":
				if num2 != 0:
					result = num1 / num2
					print(f"The result of {num1} / {num2} is {result}")
				else:
					print("Error: Division by zero is not allowed.")
			elif operation == "remainder":
				if num2 != 0:
					quotient, remainder = custom_operation(num1, num2)
					print(f"The result of {num1} ~ {num2} is quotient: {quotient} and remainder: {remainder}")
				else:
					print("Error: Division by zero is not allowed.")
			else:
				print("Invalid operation. Please choose add, subtract, multiply, divide, or 'a~b for custom operation.")
		
		calculation_type = input("What do you want to calculate? (Enter 'a~b' for custom operation): ").strip().lower()
		if calculation_type == 'a~b':
			try:
				a = float(input("Enter the first number (a): "))
				b = float(input("Enter the second number (b): "))
				quotient, remainder = custom_operation(a, b)
				print(f"The result of {a} ~ {b} is quotient: {quotient} and remainder: {remainder}")
			except ValueError:
				print("Invalid input. Please enter numbers.")
			except ValueError:
				print("Invalid input. Please enter numbers.")
		elif calculation_type == 'single':
			try:
				a = float(input("Enter a single number: "))
			# Add any specific single number calculations here if needed
			except ValueError:
				print("Invalid input. Please enter a number.")
			break
		# Ask if the user wants to perform another calculation
		another = input("Do you need another calculation? (yes/no): ").strip().lower()
		if another != 'yes':
			print(
				"Thank you for using the calculator. Goodbye © Masterschool, Owner of Software Engineering Section, 2024!")
	# Ask the user what they want to calculate from range a to b


def advanced_calculate():
	allowed_functions = {
		'sqrt': math.sqrt,
		'sin': lambda x: math.sin(math.radians(x)),
		'cos': lambda x: math.cos(math.radians(x)),
		'tan': lambda x: math.tan(math.radians(x)),
		'log': math.log,
		'log10': math.log10,
		'exp': math.exp,
		'asin': lambda x: math.degrees(math.asin(x)),
		'acos': lambda x: math.degrees(math.acos(x)),
		'atan': lambda x: math.degrees(math.atan(x)),
		'sinh': math.sinh,
		'cosh': math.cosh,
		'tanh': math.tanh,
		'asinh': math.asinh,
		'acosh': math.acosh,
		'atanh': math.atanh,
		'pi': math.pi,
		'e': math.e,
	}
	
	while True:
		text_input = input(
			"Please enter a mathematical expression (e.g., sqrt(25), sin(30), log(10), etc.) or type 'back' to return to basic operations, 'exit' to quit: ").strip().lower()
		if text_input == 'back':
			break
		if text_input == 'exit':
			print("Exiting the program. Goodbye © Masterschool, Owner of Software Engineering Section, 2024!")
			exit()
		try:
			result = eval(text_input, {"__builtins__": None}, allowed_functions)
			print(f"The result of the calculation '{text_input}' is: {result}")
		except Exception as e:
			print(f"Error: {e}")


# Display available functions
print(
	"You can use functions like sqrt, sin, cos, tan, log, log10, exp, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, pi, e")

perform_calculations()
