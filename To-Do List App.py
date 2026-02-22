def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)

def main():
    tasks = []

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()