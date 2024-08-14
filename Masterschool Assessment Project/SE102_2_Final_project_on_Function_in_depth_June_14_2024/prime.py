def is_prime(num):
	if num <= 1:
		return False
	if num == 2:
		return True  
	if num % 2 == 0:
		return False  
	for i in range(3, int(num ** 0.5) + 1, 2):
		if num % i == 0:
			return False
	return True
def print_primes_in_range(m, n):
	print(f"Prime numbers between {m} and {n}:")
	for num in range(m, n + 1):
		if is_prime(num):
			print(f"The number {num} is prime")
# Input section
start_range = int(input("Enter start range: "))
end_range = int(input("Enter end range: "))
print_primes_in_range(start_range, end_range)
