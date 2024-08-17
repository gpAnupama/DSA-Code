class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, position):
        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            return

        for i in range(position - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None or temp.next is None:
            return

        next = temp.next.next
        temp.next = next

    def print_list(self):
        tnode = self.head
        while tnode:
            print(tnode.data, end=' ')
            tnode = tnode.next
        print()

if __name__ == "__main__":
    llist = LinkedList()

    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.push(50)
    llist.push(60)
    llist.push(70)
    llist.push(80)
    llist.push(90)
    llist.push(100)

    print("\nLinked list before:")
    llist.print_list()

    llist.delete_node(2)  # Delete node at position 2
    llist.delete_node(4)  # Delete node at position 4
    llist.delete_node(6)  # Delete node at position 6

    print("\nLinked list after deletion:")
    llist.print_list()
