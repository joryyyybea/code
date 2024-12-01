tasks = []

while True:
    print("\nTo-do List Menu:")
    print("1. View To-do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        # Display all current tasks
        if not tasks:
            print("No tasks available")
        else: 
            print("\nList of Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    
    elif choice == '2':
        # Add a new task to the list
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.\n")
    
    elif choice == '3':
        # Mark a task as completed, which removes it from the list
        if not tasks:
            print("No tasks available")
        else:
            print("\nList of Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            
            try:
                task_number = int(input("Enter the number of the task to mark as completed: "))
                if 1 <= task_number <= len(tasks):
                    completed_task = tasks.pop(task_number - 1)
                    print(f"Task '{completed_task}' has been marked as completed and removed from the list.\n")
                else:
                    print("Invalid task number. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    elif choice == '4':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")