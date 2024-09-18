# Write a program in Python to check a triangle is equilateral,scalene or isosclees.
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 != side2 != side3:
    print("The triangle is scalene.")
else:
    print("The triangle is isosceles.")