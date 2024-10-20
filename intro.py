tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def show_tasks():
    print("Your tasks:")
    for task in tasks:
        print(f"- {task}")

while True:
    print("\n1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
