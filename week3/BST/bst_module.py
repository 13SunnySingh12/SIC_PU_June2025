# bst_module.py

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                print(f"Node {data} found in the tree.")
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        print(f"Node {data} not found in the tree.")
        return False

    def delete_node(self):
        data = int(input('Enter data of the node to be deleted: '))
        temp1 = self.root
        temp2 = None

        while temp1 is not None and temp1.data != data:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right

        if temp1 is None:
            print(f'Node with data {data} not found.')
            return

        print(f'Node with data {temp1.data} deleted.')

        if temp1.left is None and temp1.right is None:
            if temp1 is self.root:
                self.root = None
            elif temp2.left == temp1:
                temp2.left = None
            else:
                temp2.right = None

        elif temp1.left is None or temp1.right is None:
            child = temp1.left if temp1.left is not None else temp1.right
            if temp1 is self.root:
                self.root = child
            elif temp2.left == temp1:
                temp2.left = child
            else:
                temp2.right = child

        else:
            successor_parent = temp1
            successor = temp1.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            temp1.data = successor.data

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
