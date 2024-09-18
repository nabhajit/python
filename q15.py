# Write a program in Python to implement a simple calculator.
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

if choice in [1, 2, 3, 4]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"The difference between {num1} and {num2} is: {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
    elif choice == 4:
        result = divide(num1, num2)
        print(f"The division of {num1} by {num2} is: {result}")
else:
    print("Invalid choice. Please select a valid option (1-4).")