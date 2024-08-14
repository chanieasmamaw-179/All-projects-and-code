def print_triangle(n):
	for x in range(1, n + 1):
		for j in range(1, x + 1):
			print(j, end=' ')
		print()
	
	for x in range(n - 1, 0, -1):
		for j in range(1, x + 1):
			print(j, end=' ')
		print()


def print_multiplication_table(n):
	# Print the header row
	print("    ", end="")
	for i in range(1, n + 1):
		print(f"{i:4}", end="")
	print("\n" + "----" * (n + 1))
	
	# Print each row of the multiplication table
	for i in range(1, n + 1):
		print(f"{i:2} |", end="")
		for j in range(1, n + 1):
			print(f"{i * j:4}", end="")
		print()


while True:
	triangle_input = input("Enter the number for the triangle (-1 to exit): ")
	triangle_input = int(triangle_input)
	
	if triangle_input == -1:
		print("Bye")
		break
	
	print_triangle(triangle_input)
	
	multiplication_table_input = input("Enter the number for the multiplication table (-1 to exit): ")
	multiplication_table_input = int(multiplication_table_input)
	
	if multiplication_table_input == -1:
		print("Bye")
		break
	
	print_multiplication_table(multiplication_table_input)
