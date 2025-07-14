# Implementation of Stack using a Doubly Linked List (DLL)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLLStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.prev = self.top
            self.top.next = new_node
            self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(f"Popped: {self.top.data}")
            self.top = self.top.prev
            if self.top is not None:
                self.top.next = None

    def display(self):
         if self.top is None:
            print("Stack is empty")
         else:
            current = self.top
            print("Stack elements (Top to Bottom):")
            while current:
                print(current.data)
                current = current.prev


if __name__ == "__main__":
    stack = DLLStack()

    while True:
        print("\n=== Stack Using Doubly Linked List ===")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                value = int(input("Enter value to push: "))
                stack.push(value)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.display()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select between 1-4.")
