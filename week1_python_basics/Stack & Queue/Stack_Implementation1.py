#Implement Stack using List (Insert/Delete from Rear)

stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} into the stack.")

def pop():
    if not is_empty():
        removed_item = stack.pop()
        print(f"Popped {removed_item} from the stack.")
        return removed_item
    else:
        print("Stack is empty!")

def peek():
    if not is_empty():
        print(f"Top of the stack: {stack[-1]}")
        return stack[-1]
    else:
        print("Stack is empty!")

def is_empty():
    return len(stack) == 0

      
def display():
    if is_empty():
        print("Stack is empty.")
    else:
        print("Current Stack (Top to Bottom):")
        for item in stack[::-1]:
            print(item)



while True:
    print("\n==== Stack Menu ====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        try:
            value = int(input("Enter value to push: "))
            push(value)
        except ValueError:
            print("Please enter a valid integer.")
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please enter 1 to 5.")

