def prime_number(num):
    """
    Determine if a number is a prime number.

    Argument:
    number (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_of_two_prime_numbers(num):
    """
    Determine if a number can be expressed as the sum of two prime numbers.

    Argument:
    number (int): The number to check.

    Returns:
    bool: True if the number can be expressed as the sum of two prime numbers, False otherwise.
    """
    if num % 2 == 1:
        return False

    found = False
    for i in range(2, num // 2 + 1):
        if prime_number(i):
            j = num - i
            if prime_number(j):
                print(f"The number {num} equals the sum of {i} and {j}.")
                found = True
    return found


def main():
    """
    Main function to get user input and check if the number can be expressed as the sum of two prime numbers.

    Argument:
    None

    Returns:
    None
    """
    number = int(input("Enter the number: "))
    result = sum_of_two_prime_numbers(number)
    if not result:
        print(f"The number {number} cannot be expressed as the sum of two prime numbers.")


if __name__ == '__main__':
    main()
