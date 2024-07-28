class Queue:
    def __init__(self, max_size=4):
        self.MAXSIZE = max_size
        self.items = [None] * self.MAXSIZE
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.rear == self.MAXSIZE - 1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    def enQueue(self, element):
        if self.isFull():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.items[self.rear] = element
            print(f"Inserted {element}")

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            element = self.items[self.front]
            if self.front >= self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
            print(f"Deleted {element}")
            return element

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.items[i], end="  ")
            print()

# Testing the Queue class
if __name__ == "__main__":
    q = Queue()

    q.deQueue()  # Queue Empty

    q.enQueue(15)
    q.enQueue(38)
    q.enQueue(45)
    q.enQueue(51)
    q.enQueue(69)  # This will show "Queue is full" since the max size is 4

    q.deQueue()

    q.display()
