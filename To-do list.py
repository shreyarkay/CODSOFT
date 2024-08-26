tasks=[
    {"task": "Write", "completed": False},
    {"task": "Dance", "completed": True},
    {"task": "Exercise", "completed": True},
]

def addTask():
    task = input("Enter task: ")    
    tasks.append({"task": task, "completed": False})
    print(f"Task {task} has been added.")

def deleteTask():
    task=input("Enter task to delete: ")
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            print(f"Task '{task}' has been removed.")
            return
    print("Task not found!")

def listTask():
    if tasks:
        print("Tasks:")
        for i, t in enumerate(tasks):
            status = "Completed" if t["completed"] else "Pending"
            print(f"{i + 1}. {t['task']} - {status}")
    else:
        print("No tasks found.")
  
def completedTask():
  listTask()
  try:
    task_index=int(input("Enter task number-1 to mark as completed: ")) 
    if 0<=task_index < len(tasks):
        if not tasks[task_index]["completed"]:
            tasks[task_index]["completed"]=True
            print("Task marked as completed")
        else:
            print("Task already completed")
    else:
        print("Invalid entry!")
  except ValueError:
      print("Enter valid number!")  
if __name__ == "__main__":
    #create a loop to run the app
    print("Welcome to TO-DO LIST")
    while True:
        print("\n")
        print("Please select one of the following options: ")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Mark task as complete")
        print("5. Exit")

        choice=input("Enter your choice: ")

        if (choice=="1"):
            addTask()

        elif(choice=="2"):
            deleteTask()

        elif(choice=="3"):
            listTask()
        
        elif(choice=="4"):
            completedTask()

        elif(choice=="5"):
            print("Exiting..")
            break
        else:
            print("Invalid entry!")