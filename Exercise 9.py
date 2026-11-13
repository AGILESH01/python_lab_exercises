# Student Grading System
name = input("Enter student name: ")
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("\nStudent:", name)
print("Average:", round(average, 2))
print("Grade:", grade)
