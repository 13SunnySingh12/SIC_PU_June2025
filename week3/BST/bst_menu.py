
from bst_module import BST

def main():
    
    bst = BST()

    while True:
        print("\n----- Binary Search Tree Menu -----")
        print("1. Add Node")
        print("2. Search Node")
        print("3. Delete Node")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter number to insert: "))
            bst.insert(num)
        elif choice == '2':
            num = int(input("Enter number to search: "))
            bst.search(num)
        elif choice == '3':
            bst.delete_node()
        elif choice == '4':
            print("Inorder Traversal:")
            bst.inorder(bst.root)
            print()
        elif choice == '5':
            print("Preorder Traversal:")
            bst.preorder(bst.root)
            print()
        elif choice == '6':
            print("Postorder Traversal:")
            bst.postorder(bst.root)
            print()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
