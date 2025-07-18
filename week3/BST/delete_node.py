def delete_node(self):
    data = int(input('Enter data of the node to be deleted: '))
    temp1 = self.root
    temp2 = None

    # Search for the node
    while temp1 is not None and temp1.data != data:
        temp2 = temp1
        if data < temp1.data:
            temp1 = temp1.left
        else:
            temp1 = temp1.right

    # If node not found
    if temp1 is None:
        print(f'Node with data {data} not found.')
        return

    print(f'Node with data {temp1.data} deleted.')

    # Case 1: Node is a leaf node
    if temp1.left is None and temp1.right is None:
        if temp1 is self.root:
            self.root = None
        elif temp2.left == temp1:
            temp2.left = None
        else:
            temp2.right = None

    # Case 2: Node has one child
    elif temp1.left is None or temp1.right is None:
        child = temp1.left if temp1.left else temp1.right
        if temp1 is self.root:
            self.root = child
        elif temp2.left == temp1:
            temp2.left = child
        else:
            temp2.right = child

    # Case 3: Node has two children
    else:
        # Find inorder successor (smallest in right subtree)
        successor_parent = temp1
        successor = temp1.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace data
        temp1.data = successor.data

        # Delete successor node
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
