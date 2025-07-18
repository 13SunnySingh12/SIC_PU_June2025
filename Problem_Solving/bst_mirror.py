class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def mirror(self, root):
        if root:
            root.left, root.right = self.mirror(root.right), self.mirror(root.left)
        return root

if __name__ == '__main__':
    bst = BST()

    try:
        user_input = input("Enter space-separated integers for BST: ")
        values = list(map(int, user_input.strip().split()))

        for val in values:
            bst.root = bst.insert(bst.root, val)

        print("\nOriginal BST (Inorder):")
        bst.inorder(bst.root)

        bst.root = bst.mirror(bst.root)

        print("\nMirrored BST (Inorder):")
        bst.inorder(bst.root)
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")
