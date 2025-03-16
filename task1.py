# Task 1: Perform Basic Mathematical Operations

def perform_operations(num1, num2):
    # Addition
    addition = num1 + num2
    # Subtraction
    subtraction = num1 - num2
    # Multiplication
    multiplication = num1 * num2
    # Division
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"
    
    # Display results
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    perform_operations(num1, num2)