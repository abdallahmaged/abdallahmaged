def to_do_list():
    print("Welcome to the To-Do List App!")

    print("Choose an option: ")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    tasks = []
    choice = 0

    while choice != 4:
        choice = input("Enter your choice (1-4): ")
        

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")

# print("--------------------------------------------")

        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
                
            else:
                print("Your tasks:")
                i = 1
                for task in tasks:
                    print(i,task)
                    i+=1


# print("--------------------------------------------")


        elif choice == "3":
            if not tasks:
                print("No tasks to delete!")

            else:
                print("Your tasks:")
                i = 1
                for task in tasks:
                    print(i,task)
                    i+=1
                task_num = input("Enter the number you want to delete: ")

                task_num = int(task_num)

                if task_num >= 1 and task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1) 
                    print(f"Deleted:{deleted}")
                else:
                    print("Invalid task number") 


# print("--------------------------------------------")


        elif choice == "4":
            print("Goodbye!")
            break

# print("--------------------------------------------")

        else:
            print("Invalid choice.Please try again.") 

to_do_list()