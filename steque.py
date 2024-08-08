class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Steque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Steque is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return item

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def peek(self):
        if self.is_empty():
            raise IndexError("Steque is empty")
        return self.front.data

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_reverse(self):
        current = self.rear
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

# Example usage
steque = Steque()
steque.push(10)         # Push 10
steque.push(20)         # Push 20
steque.enqueue(30)      # Enqueue 30
steque.enqueue(40)      # Enqueue 40

# Display the steque contents from front to rear
print("Steque (front to rear):", steque.display())  # Output: [20, 10, 30, 40]

# Display the steque contents from rear to front
print("Steque (rear to front):", steque.display_reverse())  # Output: [40, 30, 10, 20]

# Pop an element
print("Popped element:", steque.pop())  # Output: 20

# Display the steque contents after popping
print("Steque after pop (front to rear):", steque.display())  # Output: [10, 30, 40]
