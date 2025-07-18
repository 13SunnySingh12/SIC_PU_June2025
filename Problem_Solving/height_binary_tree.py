class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    
    elif data <= root.data:
        root.left = insert(root.left, data) 
    
    else:
        root.right = insert(root.right, data)

    return root

def height(root):
    if root is None:
        return -1
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return 1 + max(left_height, right_height)
    
number_of_nodes = int(input("Enter number of nodes: "))
node_values = list(map(int, input("Enter node values: ").split()))
root = None
for data in node_values:
    root = insert(root, data)

print(height(root)) 
