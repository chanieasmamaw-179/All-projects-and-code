def is_prime(number):
	if number <= 1:
		return False
	if number <= 3:
		return True
	if number % 2 == 0 or number % 3 == 0:
		return False
	i = 5
	while i * i <= number:
		if number % i == 0 or number % (i + 2) == 0:
			return False
		i += 6
	return True


def is_sum_of_two_prime_numbers(number):
	if number % 2 == 1:
		return False
	
	found = False
	for i in range(2, number):
		if is_prime(i):
			j = number - i
			if is_prime(j):
				print(f"The number {number} equals the sum of {i} and {j}.")
				found = True
	return found


number = int(input("Enter the number: "))
result = is_sum_of_two_prime_numbers(number)
if not result:
	print(f"The number {number} cannot be expressed as the sum of two prime numbers.")
