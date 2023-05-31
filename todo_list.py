def display_menu():
    print("Todo List Manager")
    print("-----------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task_name = input("Enter task name: ")
    tasks.append(task_name)
    print("Task added successfully!")


def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_task_complete(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index] += " (Complete)"
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task}' deleted!")
    else:
        print("Invalid task index.")


def main():
    tasks = []  # List to store tasks
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
