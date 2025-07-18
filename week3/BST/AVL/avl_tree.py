class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class avl:
    def height(self, node):
        return 0 if node is None else node.height

    def balance(self, node):
        return 0 if node is None else self.height(node.left) - self.height(node.right)

    def rotate_right(self, root):
        new_root = root.left
        moved_sub = new_root.right

        new_root.right = root
        root.left = moved_sub

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

        return new_root

    def rotate_left(self, root):
        new_root = root.right
        moved_sub = new_root.left

        new_root.left = root
        root.right = moved_sub

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))

        return new_root

    def insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            print("Duplicate keys are not allowed.")
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        bal = self.balance(node)

        if (bal > 1) and (key < node.left.key):
            return self.rotate_right(node)
        elif (bal < -1) and (key > node.right.key):
            return self.rotate_left(node)
        elif (bal > 1) and (key > node.left.key):
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif (bal < -1) and (key < node.right.key):
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self.min_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        bal = self.balance(node)

        if (bal > 1) and (self.balance(node.left) >= 0):
            return self.rotate_right(node)
        elif (bal > 1) and (self.balance(node.left) < 0):
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif (bal < -1) and (self.balance(node.right) <= 0):
            return self.rotate_left(node)
        elif (bal < -1) and (self.balance(node.right) > 0):
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")
