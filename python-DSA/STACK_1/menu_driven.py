stack = []

def push():
    item = input("Enter the Element that will be push: \n")
    stack.append(item)
    print("Push operation successful.")

def pop():
    if not stack:
        print("The stack is empty, nothing to pop.")
    else:
        item = stack.pop()
        print("The popped element is:", item)

def display():
    if not stack:
        print("The stack is empty.")
    else:
        print("Stack elements:", stack)

def count():
    length = len(stack)
    print("The stack length is:", length)

def switch_case(choice):
    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        count()

while True:
    choice = input("\nEnter 1 for Push:\nEnter 2 for Pop:\nEnter 3 for Display:\nEnter 4 for Count:\n")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue
    
    switch_case(choice)
