# data_structures/recursion/recursion.py

class Recursion:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def power(self, base, exponent):
        if exponent == 0:
            return 1
        return base * self.power(base, exponent - 1)


# Example usage:
if __name__ == "__main__":
    recursion = Recursion()

    # Factorial
    # Output: Factorial of 5: 120
    print("Factorial of 5:", recursion.factorial(5))

    # Fibonacci
    print("Fibonacci sequence up to 8 terms:")
    for i in range(8):
        print(recursion.fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5 8 13
    print()

    # Power
    # Output: 2 raised to the power of 5: 32
    print("2 raised to the power of 5:", recursion.power(2, 5))
