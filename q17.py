# Write a program in Python to print 1 to n.
def print_numbers(n):
    if n > 1:
        print_numbers(n-1)
    print(n)

n = int(input("Enter the value of n: "))
print_numbers(n)