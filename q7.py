# write a program in Python to convert a given number of days into days, month, year and week.
days = int(input("Enter number of days: "))

years = days // 365
remaining_days = days % 365
months = remaining_days // 30
remaining_days = remaining_days % 30
weeks = remaining_days // 7
remaining_days = remaining_days % 7

print(f"{days} days is equivalent to {years} years, {months} months, {weeks} weeks, and {remaining_days} days.")