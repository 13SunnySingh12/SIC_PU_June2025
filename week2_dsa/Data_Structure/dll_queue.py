# Implementation of  Queue using a Doubly Linked List (DLL)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLLQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Inserted: {data}")

    def delete(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(f"Deleted: {self.front.data}")
            self.front = self.front.next
            if self.front is not None:
                self.front.prev = None
            else:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            current = self.front
            print("Queue elements:")
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")


if __name__ == "__main__":
    queue = DLLQueue()

    while True:
        print("\n=== Doubly Linked List Queue ===")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                value = int(input("Enter value to insert: "))
                queue.insert(value)
            except ValueError:
                print("Invalid input. Enter an integer.")
        elif choice == "2":
            queue.delete()
        elif choice == "3":
            queue.display()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select between 1-4.")
