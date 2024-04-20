# data_structures/queues/priority_queues.py

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data, priority):
        self.queue.append((data, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.queue.pop(0)[0]

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[0][0]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        for item in self.queue:
            print(item[0], end=" ")
        print()


# Example usage:
if __name__ == "__main__":
    queue = PriorityQueue()
    queue.enqueue("Task 1", 2)
    queue.enqueue("Task 2", 1)
    queue.enqueue("Task 3", 3)
    queue.display()  # Output: Queue elements: Task 2 Task 1 Task 3

    print("Front element:", queue.peek())  # Output: Front element: Task 2

    queue.dequeue()
    queue.display()  # Output: Queue elements: Task 1 Task 3
