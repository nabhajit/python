#  Take marks of a student of four different subject find average depending on average find Grade.
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))

average = (subject1 + subject2 + subject3 + subject4) / 4

if average >= 75:
    grade = 'A'
elif average >= 60:
    grade = 'B'
elif average >= 40:
    grade = 'C'
else:
    grade = 'D'

print(f"Average marks: {average}")
print(f"Grade: {grade}")