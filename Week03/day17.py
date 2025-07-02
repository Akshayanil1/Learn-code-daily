filename = "tasks.txt"

def save_tasks_to_file(task_list):
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")
def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            clean_tasks = []
            lines_from_file = file.readlines()
            for line in lines_from_file:
                clean_tasks.append(line.strip())
            return clean_tasks
    except FileNotFoundError:
        print("No saved tasks found. Starting with a new list.")
        return[]

task_list = ["Buy groceries", "Complete homework", "Call mom"]
def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

def add_task(task_list, new_task):
    task_list.append(new_task)
    print(f"New_task {new_task} added successfully.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

# Load tasks from file at the start
tasks = load_tasks_from_file()

while True:
    display_menu()
    choice = input("Enter your choice (1-3): ")     

    if choice == "1":
        new_task = input("Enter new task: ")
        add_task(tasks, new_task)
        save_tasks_to_file(tasks)  # Save after adding
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        print("Exiting the To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")      