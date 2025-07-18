from avl_tree import avl

def main():
    tree = avl()
    root = None

    while True:
        print("\n=== AVL Tree Menu ===")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            key = int(input("Enter value to insert: "))
            root = tree.insert(root, key)
        elif choice == "2":
            key = int(input("Enter value to delete: "))
            root = tree.delete(root, key)
        elif choice == "3":
            key = int(input("Enter value to search: "))
            found = tree.search(root, key)
            print("Found." if found else "Not found.")
        elif choice == "4":
            print("Inorder: ", end="")
            tree.inorder(root)
            print()
        elif choice == "5":
            print("Preorder: ", end="")
            tree.preorder(root)
            print()
        elif choice == "6":
            print("Postorder: ", end="")
            tree.postorder(root)
            print()
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1–7.")


if __name__ == "__main__":
    main()
