# Student Data Manager using Files
name = input("Enter student name: ")
mark = input("Enter student mark: ")

with open("students.txt", "a") as file:
    file.write(name + "," + mark + "\n")

print("\nStudent record saved.")
print("Saved student records:")

with open("students.txt", "r") as file:
    for record in file:
        print(record.strip())
