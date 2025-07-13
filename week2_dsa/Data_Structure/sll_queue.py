# Implementation of Queue using a Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class SLLQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = new_node
        print(f"Inserted: {data}")

    def delete(self):
        if self.front is None:
            print("Queue is empty. Cannot delete.")
        else:
            print(f"Deleted: {self.front.data}")
            self.front = self.front.link
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            current = self.front
            print("Queue elements:")
            while current:
                print(current.data, end=" -> ")
                current = current.link
            print("None")



if __name__ == "__main__":
    queue = SLLQueue()

    while True:
        print("\n=== Queue Operations ===")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                value = int(input("Enter value to insert: "))
                queue.insert(value)
            except:
                print("Please enter a valid integer.")
        elif choice == "2":
            queue.delete()
        elif choice == "3":
            queue.display()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select between 1-4.")
