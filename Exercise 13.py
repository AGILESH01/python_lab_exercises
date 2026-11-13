# CSV-Based Payroll Management System
import csv
import os

name = input("Enter employee name: ")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
salary = hours * rate

file_exists = os.path.exists("payroll.csv")

with open("payroll.csv", "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Name", "Hours", "Rate", "Salary"])
    writer.writerow([name, hours, rate, salary])

print("\nPayroll record saved.")
print("Employee:", name)
print("Salary:", round(salary, 2))
