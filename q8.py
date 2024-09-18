# Write a Python Program to find the gravitational force acting between two objects.
m1 = float(input("Enter the mass of the first object (in kg): "))
m2 = float(input("Enter the mass of the second object (in kg): "))
r = float(input("Enter the distance between the centers of the two objects (in meters): "))

G = 6.67430e-11
F = (G * m1 * m2) / (r ** 2)

print(f"The gravitational force between the two objects is: {F} N")