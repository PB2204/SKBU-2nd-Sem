# data_structures/linked_lists/cll.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        if current.data == data:
            prev.next = self.head

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")


# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.prepend(0)
    cll.display()  # Output: 0 -> 1 -> 2 -> 3 -> Head

    cll.delete(2)
    cll.display()  # Output: 0 -> 1 -> 3 -> Head

    print("Is 3 in the list?", cll.search(3))  # Output: True
