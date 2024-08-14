
def triangle_numbers(n):
    for a in range(1, n + 1):
        for j in range(1, a + 1):
            print(j, end=' ')
        print()

# Example usage:
triangle_numbers(20)

