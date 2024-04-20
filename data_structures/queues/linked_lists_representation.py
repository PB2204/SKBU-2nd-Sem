# data_structures/queues/linked_lists_representation.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
if __name__ == "__main__":
    queue = QueueLinkedList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()  # Output: Queue elements: 1 2 3

    print("Front element:", queue.peek())  # Output: Front element: 1

    queue.dequeue()
    queue.display()  # Output: Queue elements: 2 3
