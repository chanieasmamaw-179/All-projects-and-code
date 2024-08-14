import math
from datetime import date

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
    +     Nitzan Smulevici                                               +
    +     software Engineer/software Developer                                +
    *     nitzan@faculty.masterschool.com                                     *
    #**************************************+++++++++++++++++++++++++++++++++++#
    """
	print(message)


# Get user input
user_name = "This is one of power of python application"
welcome_message(user_name)

print("Welcome to the Python calculator!")


def perform_calculations():
	while True:
		try:
			num_calculations = int(input("How many calculations do you want to perform? "))
		except ValueError:
			print("Invalid input. Please enter an integer.")
			continue
		try:
			calculation_type = input(
				"Do you want basic or advanced calculation? Type 'basic' or 'advanced': ").strip().lower()
			if calculation_type == 'basic':
				basic_calculate(num_calculations)
			elif calculation_type == 'advanced':
				advanced_calculate()
			else:
				print("Invalid input. Please type 'basic' or 'advanced'.")
				continue
		except ValueError:
			print("Invalid input. Please enter a valid calculation type.")
			continue
		# Ask if the user wants to perform another calculation
		another = input("Do you need another calculation? (yes/no): ").strip().lower()
		if another != 'yes':
			print(
				"Thank you for using the calculator. Goodbye © Masterschool, Owner of Software Engineering Section, 2024!")
			break


def basic_calculate(num_calculations):
	for _ in range(num_calculations):
		try:
			operation = input(
				"Enter an arithmetic expression (e.g., 2+3, 7~2) or type 'back' to return to main menu: ").strip().lower()
			if operation == 'back':
				break
			elif operation == 'exit':
				print("Exiting the program. Goodbye © Masterschool, Owner of Software Engineering Section, 2024!")
				exit()
			# Handling custom operation 7~2
			if '~' in operation:
				parts = operation.split('~')
				if len(parts) == 2:
					a = int(parts[0])
					b = int(parts[1])
					quotient, remainder = divmod(a, b)
					print(f"The result of {operation} is quotient: {quotient} and remainder: {remainder}")
					continue
			# Evaluating other arithmetic expressions
			result = eval(operation)
			print(f"The result of {operation} is {result}")
		
		except Exception as e:
			print(f"Error: {e}")
			continue


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
		try:
			text_input = input(
				"Please enter a mathematical expression (e.g., sqrt(25), sin(30), log(10), etc.) or type 'back' to return to main menu, 'exit' to quit: ").strip().lower()
			
			if text_input == 'back':
				break
			elif text_input == 'exit':
				print("Exiting the program. Goodbye © Masterschool, Owner of Software Engineering Section, 2024!")
				exit()
			
			result = eval(text_input, {"__builtins__": None}, allowed_functions)
			print(f"The result of the calculation '{text_input}' is: {result}")
		
		except Exception as e:
			print(f"Error: {e}")
			continue


# Display available functions


# Start performing calculations
perform_calculations()
