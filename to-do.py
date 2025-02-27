def main():
    tasks = []

    while True:
        print("\n========= To-Do APPLICATION =========")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':  # Add Task
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == '2':  # Show Tasks
            if not tasks:
                print("No tasks to show.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == '3':  # Delete Task
            if not tasks:
                print("No tasks to delete.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                task_num = input("Enter task number to delete: ")

                # Check if input is valid
                if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                    tasks.pop(int(task_num) - 1)
                    print("Task deleted!")
                else:
                    print("Invalid task number.")

        elif choice == '4':  # Exit
            print("Exiting To-Do Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
