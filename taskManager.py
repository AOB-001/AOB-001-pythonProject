tasks = []

def addTask():
    task = input("Enter task description: ")
    tasks.append(task) 
    print("********************") 
    print("Task added successfully!")

def markAsCompleted():
    if not tasks:
        print("********************")
        print("No tasks available.")
        return
    
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    
    try:
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        if index < 0 or index >= len(tasks):
            print("********************")
            print("Invalid index.")
        else:
            tasks[index] = f"{tasks[index]} (Completed)"
            print("********************")
            print("Task marked as completed.")
    except ValueError:
        print("********************")
        print("Invalid input. Please enter a valid index.")

def displayTasks():
    if not tasks:
        print("********************")
        print("Sorry!, there is no tasks available, press 1 to add")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def removeTasks():
    if not tasks:
        print("********************")
        print("Sorry!, there is no tasks available, press 1 to add")
        return
    
    print("Your Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    
    try:
        print("********************")
        index = int(input("Enter the index of the task to remove: ")) - 1
        if index < 0 or index >= len(tasks):
            print("********************")
            print("Invalid index.")
        else:
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully.")
    except ValueError:
        print("********************")
        print("Invalid input. Please enter a valid index.")

def displayMenu():
    print('\n')
    print("<< Task Manager >>\n")
    print("1 --> Add Task")
    print("2 --> Mark Task as Completed")
    print("3 --> Display Tasks")
    print("4 --> Remove Task")
    print("5 --> Exit\n")

def main():
    while True:
        displayMenu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("********************")
            addTask()
            print("********************")
        elif choice == '2':
            print("********************")
            markAsCompleted()
            print("********************")
        elif choice == '3':
            print("********************")
            displayTasks()
            print("********************")
        elif choice == '4':
            print("********************")
            removeTasks()
            print("********************")
        elif choice == '5':
            print("********************")
            print("Exiting the program...")
            print("********************")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
main()