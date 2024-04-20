# data_structures/stacks/array_representation.py

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

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack elements:")
        for i in range(self.top, -1, -1):
            print(self.stack[i])
        print()


# Example usage:
if __name__ == "__main__":
    stack = StackArray(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()  # Output: Stack elements: 3 2 1

    print("Top element:", stack.peek())  # Output: Top element: 3

    stack.pop()
    stack.display()  # Output: Stack elements: 2 1
