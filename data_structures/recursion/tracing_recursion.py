# data_structures/recursion/tracing_recursion.py

class TracingRecursion:
    def factorial(self, n):
        print("Calculating factorial of", n)
        if n == 0 or n == 1:
            return 1
        result = n * self.factorial(n - 1)
        print("Factorial of", n, "is", result)
        return result

    def fibonacci(self, n):
        print("Calculating Fibonacci of", n)
        if n <= 1:
            return n
        result = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        print("Fibonacci of", n, "is", result)
        return result

    def power(self, base, exponent):
        print("Calculating", base, "raised to the power of", exponent)
        if exponent == 0:
            return 1
        result = base * self.power(base, exponent - 1)
        print(base, "raised to the power of", exponent, "is", result)
        return result


# Example usage:
if __name__ == "__main__":
    tracing_recursion = TracingRecursion()

    # Factorial
    print("Factorial of 5:", tracing_recursion.factorial(5))
    print()

    # Fibonacci
    print("Fibonacci sequence up to 8 terms:")
    for i in range(8):
        print(tracing_recursion.fibonacci(i), end=" ")
    print()
    print()

    # Power
    print("2 raised to the power of 5:", tracing_recursion.power(2, 5))
