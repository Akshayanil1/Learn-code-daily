# tasks = []
# def display_menu():
#     print("Task Manager")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Exit")

# def add_task(task_list, new_task):
#     task_list.append(new_task)
#     print(f"New task {new_task} added successfully.")

# def view_tasks(task_list):
#     print("\n--- Your To-Do List ---")
#     if not task_list:
#         print("No tasks found.")
#     else:
#         for index, task in enumerate(task_list, start=1):
#             print(f"--- {index}. {task} ---")

# while True:
#     display_menu()
#     choice = input("Enter your chhoice (1-3): ")

#     if choice == "1":
#         new_task = input("Enter the new task: ")
#         add_task(tasks, new_task)
#     elif choice == "2":
#         view_tasks(tasks)
#     elif choice == "3":
#         print("Exiting the To_Do List Manager. Goodbye!")
#         break
#     else:
#         print("Invalid choice, please try again.")
    

#This code is a simple task manger which allows user to add and view tasks.
tasks = []

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
        for index, task in enumerate(task_list, start = 1):
            print(f"{index}. {task}")

while True:
    display_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        new_task = input("Enter new task: ")
        add_task(tasks, new_task)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        print("Exiting the To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")