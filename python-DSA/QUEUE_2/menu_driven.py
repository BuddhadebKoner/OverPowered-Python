Queue = []

def enqueue():
    item = input("Enter the Element that will be enqueued: \n")
    Queue.append(item)
    print("Enqueue operation successful.")

def dequeue():
    if not Queue:
        print("The Queue is empty, nothing to dequeue.")
    else:
        item = Queue.pop(0)
        print("The dequeued element is:", item)

def display():
    if not Queue:
        print("The Queue is empty.")
    else:
        print("Queue elements:", Queue)

def count():
    length = len(Queue)
    print("The Queue length is:", length)

def switch_case(choice):
    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        count()

while True:
    choice = input("\nEnter 1 for enqueue:\nEnter 2 for dequeue:\nEnter 3 for Display:\nEnter 4 for Count:\n")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue
    
    switch_case(choice)