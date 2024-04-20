# data_structures/queues/array_representation.py

class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


# Example usage:
if __name__ == "__main__":
    queue = QueueArray(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()  # Output: Queue elements: 1 2 3

    print("Front element:", queue.peek())  # Output: Front element: 1

    queue.dequeue()
    queue.display()  # Output: Queue elements: 2 3
