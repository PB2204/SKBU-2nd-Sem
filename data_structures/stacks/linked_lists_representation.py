# data_structures/stacks/linked_lists_representation.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.head.data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.head
        print("Stack elements:")
        while current:
            print(current.data)
            current = current.next
        print()


# Example usage:
if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()  # Output: Stack elements: 3 2 1

    print("Top element:", stack.peek())  # Output: Top element: 3

    stack.pop()
    stack.display()  # Output: Stack elements: 2 1
