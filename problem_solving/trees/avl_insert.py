''' Problem Title:
Insert in AVL Tree

Problem Description:
Given an initially empty AVL (Adelson-Velsky and Landis) tree, implement the insertion operation. After each insertion, ensure the tree remains balanced according to AVL tree properties. An AVL tree is a self-balancing binary search tree where the difference between heights of left and right subtrees cannot be more than one for all nodes.

Input Format:
- The first line contains an integer n, the number of elements to insert.
- The second line contains n space-separated integers, representing the values to be inserted in the given order.

Output Format:
- Print the pre-order traversal of the AVL tree after all insertions. '''


class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, z):
        y = z.left
        temp_right = y.right

        y.right = z
        z.left = temp_right

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        temp_left = y.left

        y.left = z
        z.right = temp_left

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):

        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def pre_order(self, root):
        result = []

        def traverse(node):
            if node:
                result.append(node.key)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return result



if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    tree = AVLTree()
    root = None

    for value in values:
        root = tree.insert(root, value)

    result = tree.pre_order(root)
    print(" ".join(map(str, result)))
