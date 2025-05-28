# match_case_calculator.py

# Prompt the user for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform calculation using match-case (Python 3.10+)
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from +, -, *, /.")
