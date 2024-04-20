# data_structures/stacks/utility.py

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


def check_balanced_parentheses(expression):
    stack = StackArray(len(expression))
    opening_brackets = set(['(', '[', '{'])
    closing_brackets = set([')', ']', '}'])
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if bracket_pairs[top_char] != char:
                return False
    return stack.is_empty()


def reverse_stack(stack):
    if stack.is_empty():
        return
    data = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, data)


def insert_at_bottom(stack, data):
    if stack.is_empty():
        stack.push(data)
        return
    temp = stack.pop()
    insert_at_bottom(stack, data)
    stack.push(temp)


# Example usage:
if __name__ == "__main__":
    # Check balanced parentheses
    expression = "{[()]}"
    print("Is", expression, "balanced?", check_balanced_parentheses(
        expression))  # Output: Is {[()]} balanced? True

    # Reverse a stack
    stack = StackArray(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Original stack:")
    while not stack.is_empty():
        print(stack.pop(), end=" ")
    print()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    reverse_stack(stack)
    print("Reversed stack:")
    while not stack.is_empty():
        print(stack.pop(), end=" ")
    print()
