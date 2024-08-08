def add():
     sum=a+b 
     print(f"Sum of {a} and {b} is: {sum}")

def sub():
     sub=a-b
     print(f"Subtraction of {a} and {b} is: {sub}")

def mul():
     mul=a*b
     print(f"Product of {a} and {b}  is: {mul}")

def div():
     if b==0:
        print("Division by zero error")
     else:
        div=a//b
        print(f"Divison of {a} and {b} is: {div}")

print("Calcuator")

while True:
        print("\n")
        a=int(input("Enter a number: "))
        b=int(input("Enter another number: "))
        print("Please select one of the following options: ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Continue")
        print("6. Exit")

        choice=input("Enter your choice: ")

        if (choice=="1"):
            add()

        elif(choice=="2"):
            sub()

        elif(choice=="3"):
            mul()
        
        elif(choice=="4"):
            div()

        elif(choice=="5"):
            continue

        elif(choice=="6"):
            print("Exiting..")
            break
        else:
            print("Invalid entry!")