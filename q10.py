# Take input from user, if it is greater than 15 print two times of difference, if it’s less than 15 print four times of difference.
num = int(input("Enter a number: "))

if num > 15:
    difference = num - 15
    result = 2 * difference
else:
    difference = 15 - num
    result = 4 * difference

print(f"The result is: {result}")