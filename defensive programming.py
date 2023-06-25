import os

# create a new text file
filename = "calculations.txt"
with open(filename, "w") as f:
    f.write("These are my calculations.\n")

# ask the user for input
while True:
    choice = input("Enter your choice: open file (1) or make a calculation (2)? ")
    if choice == "1":
        # ask for the filename and try to open it
        filename = input("Enter the name of the file you want to open: ")
        try:
            os.path.exists(filename)
            with open(filename, "r") as f:
                print(f.read())
        except FileNotFoundError as e:
            print(f"Error: {e}")
    elif choice == '2':
        # ask for two numbers and an operator, and perform the calculation
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            op = input("Enter the operator (+, -, *, /): ")
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2
            else:
                print("Invalid operator.")
                continue
            print(f"Result: {result}")
            with open("calculations.txt", "a") as f:
                f.write(f"{num1} {op} {num2} = {result}\n")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

