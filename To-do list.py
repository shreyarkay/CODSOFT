
tasks=[]

def addTask():
    task = input("Enter task: ")    
    tasks.append(task)
    print(f"Task {task} has been added.")

def deleteTask():
    task=input("Enter task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task {task} has been removed.")
    else:
        print("Invalid task!")

def listTask():
    print(tasks)
if __name__ == "__main__":
    #create a loop to run the app
    print("Welcome to TO-DO LIST")
    while True:
        print("\n")
        print("Please select one of the following options: ")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Exit")

        choice=input("Enter your choice: ")

        if (choice=="1"):
            addTask()

        elif(choice=="2"):
            deleteTask()

        elif(choice=="3"):
            listTask()

        elif(choice=="4"):
            break
        else:
            print("Invalid entry!")
        

        