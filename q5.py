# Write a program in Python to swap two numbers without using third variable.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")