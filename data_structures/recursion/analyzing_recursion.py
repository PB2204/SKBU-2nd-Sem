# data_structures/recursion/analyzing_recursion.py

class AnalyzingRecursion:
    def __init__(self):
        self.calls = 0

    def factorial(self, n):
        self.calls += 1
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        self.calls += 1
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def power(self, base, exponent):
        self.calls += 1
        if exponent == 0:
            return 1
        return base * self.power(base, exponent - 1)

    def get_calls(self):
        return self.calls

    def reset_calls(self):
        self.calls = 0


# Example usage:
if __name__ == "__main__":
    analyzing_recursion = AnalyzingRecursion()

    # Factorial
    analyzing_recursion.factorial(5)
    # Output: Factorial calls: 6
    print("Factorial calls:", analyzing_recursion.get_calls())
    analyzing_recursion.reset_calls()

    # Fibonacci
    analyzing_recursion.fibonacci(8)
    # Output: Fibonacci calls: 67
    print("Fibonacci calls:", analyzing_recursion.get_calls())
    analyzing_recursion.reset_calls()

    # Power
    analyzing_recursion.power(2, 5)
    # Output: Power calls: 6
    print("Power calls:", analyzing_recursion.get_calls())
