# data_structures/linked_lists/polynomial_representation.py

class Node:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_term(self, coefficient, power):
        new_node = Node(coefficient, power)
        if self.is_empty() or power > self.head.power:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.power > power:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete_term(self, power):
        if self.is_empty():
            return
        if self.head.power == power:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.power == power:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if self.is_empty():
            print("Polynomial is empty")
            return
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.power}", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()


# Example usage:
if __name__ == "__main__":
    polynomial = Polynomial()
    polynomial.insert_term(3, 2)
    polynomial.insert_term(5, 1)
    polynomial.insert_term(7, 0)
    polynomial.display()  # Output: 3x^2 + 5x^1 + 7

    polynomial.insert_term(4, 3)
    polynomial.display()  # Output: 4x^3 + 3x^2 + 5x^1 + 7

    polynomial.delete_term(1)
    polynomial.display()  # Output: 4x^3 + 3x^2 + 7
