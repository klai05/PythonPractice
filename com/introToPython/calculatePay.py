rate = int(input("What is your hourly wage? "))
hours = int(input("How many hours did you work? "))

if hours <= 40:
    pay = hours * rate
else:
    pay = hours * rate
    overtimeHours = hours - 40
    overtimePay = overtimeHours * (rate * 0.5)
    pay = pay + overtimePay

print("Your weekly pay is:", pay)