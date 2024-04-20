# data_structures/stacks/postfix.py

class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]


def evaluate_postfix(expression):
    stack = StackArray(len(expression))
    operators = set(['+', '-', '*', '/'])
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                print("Invalid expression")
                return None
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.push(result)
        else:
            print("Invalid token:", token)
            return None
    return stack.pop()


# Example usage:
if __name__ == "__main__":
    postfix_expression = "5 3 + 4 2 - *"
    result = evaluate_postfix(postfix_expression)
    print("Postfix expression:", postfix_expression)
    print("Result of postfix expression evaluation:", result)
