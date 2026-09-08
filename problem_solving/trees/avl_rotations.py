# Which rotation does each insertion trigger? Same AVL insert as avl_insert.py,
# but it prints LL / RR / LR / RL as each rebalance happens.

class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, root):
        return 0 if not root else root.height

    def get_balance(self, root):
        return 0 if not root else self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, z):
        y = z.left
        x_subtree = y.right

        y.right = z
        z.left = x_subtree

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        x_subtree = y.left

        y.left = z
        z.right = x_subtree

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

        # LL Rotation
        if balance > 1 and key < root.left.key:
            print(f"LL Rotation at node {root.key}")
            return self.right_rotate(root)

        # RR Rotation
        if balance < -1 and key > root.right.key:
            print(f"RR Rotation at node {root.key}")
            return self.left_rotate(root)

        # LR Rotation
        if balance > 1 and key > root.left.key:
            print(f"LR Rotation at node {root.key}")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Rotation
        if balance < -1 and key < root.right.key:
            print(f"RL Rotation at node {root.key}")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

if __name__ == "__main__":
    N = int(input())
    elements = list(map(int, input().split()))
    
    tree = AVLTree()
    root = None
    
    for key in elements:
        root = tree.insert(root, key)
