class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def insert_edge(tree_map, u, v, c):
    if u not in tree_map:
        tree_map[u] = Node(u)
    if v not in tree_map:
        tree_map[v] = Node(v)

    if c == 'L':
        tree_map[u].left = tree_map[v]
    else:
        tree_map[u].right = tree_map[v]

def are_mirrors(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.data != node2.data:
        return False
    return (are_mirrors(node1.left, node2.right) and
            are_mirrors(node1.right, node2.left))

# Input reading
N = int(input())

tree1_map = {}
tree2_map = {}

for _ in range(N - 1):
    u, v, c = input().split()
    insert_edge(tree1_map, int(u), int(v), c)

for _ in range(N - 1):
    u, v, c = input().split()
    insert_edge(tree2_map, int(u), int(v), c)

# Assume root is the first node inserted
root_val = int(list(tree1_map.keys())[0])
root1 = tree1_map[root_val]
root2 = tree2_map[root_val]

if are_mirrors(root1, root2):
    print("yes")
else:
    print("no")
