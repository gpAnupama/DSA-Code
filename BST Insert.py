class BSTNode:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

class BSTInsertion:
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        # If the current node is None, place the new value here
        if node is None:
            return BSTNode(value)

        # If the value is less than the current node's value, go left
        if value < node.value:
            node.leftchild = self.insert(node.leftchild, value)
        # If the value is greater, go right
        elif value > node.value:
            node.rightchild = self.insert(node.rightchild, value)

        return node

    def inorder(self, node):
        if node:
            self.inorder(node.leftchild)
            print(node.value, end=' ')
            self.inorder(node.rightchild)

if __name__ == "__main__":
    bstree = BSTInsertion()

    bstree.root = bstree.insert(bstree.root, 55)
    bstree.root = bstree.insert(bstree.root, 32)
    bstree.root = bstree.insert(bstree.root, 29)
    bstree.root = bstree.insert(bstree.root, 44)
    bstree.root = bstree.insert(bstree.root, 71)
    bstree.root = bstree.insert(bstree.root, 68)
    bstree.root = bstree.insert(bstree.root, 89)

    print("In-order traversal of the BST:")
    bstree.inorder(bstree.root)
