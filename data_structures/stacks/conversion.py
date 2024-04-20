# data_structures/stacks/conversion.py

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


def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    prefix = []
    stack = StackArray(len(expression))
    # Reverse the expression to process from right to left
    for token in expression.split()[::-1]:
        if token.isdigit():
            prefix.append(token)
        elif token == ')':
            stack.push(token)
        elif token == '(':
            while not stack.is_empty() and stack.peek() != ')':
                prefix.append(stack.pop())
            if stack.peek() == ')':
                stack.pop()  # Discard ')'
        else:
            while not stack.is_empty() and precedence.get(token, 0) < precedence.get(stack.peek(), 0):
                prefix.append(stack.pop())
            stack.push(token)
    while not stack.is_empty():
        prefix.append(stack.pop())
    # Reverse the prefix expression to get the correct order
    return ' '.join(prefix[::-1])


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    postfix = []
    stack = StackArray(len(expression))
    for token in expression.split():
        if token.isdigit():
            postfix.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            if stack.peek() == '(':
                stack.pop()  # Discard '('
        else:
            while not stack.is_empty() and precedence.get(token, 0) <= precedence.get(stack.peek(), 0):
                postfix.append(stack.pop())
            stack.push(token)
    while not stack.is_empty():
        postfix.append(stack.pop())
    return ' '.join(postfix)


# Example usage:
if __name__ == "__main__":
    infix_expression = "( 5 + 3 ) * ( 4 - 2 )"
    prefix_expression = infix_to_prefix(infix_expression)
    postfix_expression = infix_to_postfix(infix_expression)
    print("Infix expression:", infix_expression)
    print("Prefix expression:", prefix_expression)
    print("Postfix expression:", postfix_expression)
