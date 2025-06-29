#Implement Queue using list, insert front, delete from rear of the list

# Queue Implementation using List (Insert at Front, Delete from Rear)

queue = []

def enqueue(item):
    queue.insert(0,item)
    print(f"Enqueued {item} into the queue.")

def dequeue():
    if not is_empty():
        removed_item = queue.pop()
        print(f"Dequeued {removed_item} from the queue.")
        return removed_item
    else:
        print("Queue is empty.")

def peek():
    if not is_empty():
        print(f"Front of the queue: {queue[-1]}")
        return queue[-1]
    else:
        print("Queue is empty.")

def is_empty():
    return len(queue) == 0

def display():
    if is_empty():
        print("Queue is empty.")
    else:
        print("Current Queue (Front to Rear):")
        for item in queue[::-1]:
            print(item)


while True:
    print("\n==== Queue Menu ====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        try:
            value = int(input("Enter value to enqueue: "))
            enqueue(value)
        except ValueError:
            print("Please enter a valid integer.")
    elif choice == '2':
        dequeue()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please enter 1 to 5.")
