import json

# Load existing tasks from file (if any)
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"name": task_name, "completed": False})
    save_tasks()

def list_tasks():
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{i+1}. {task['name']} - {status}")

def mark_task_complete():
    list_tasks()
    task_number = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        save_tasks()
    else:
        print("Invalid task number")

def delete_task():
    list_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        del tasks[task_number]
        save_tasks()
    else:
        print("Invalid task number")

def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
