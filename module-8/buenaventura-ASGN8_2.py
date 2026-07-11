# Roxanne Buenaventura
# CSD325
# Assignment 8_2
# 10 July 2026

import json

# Function to display student information
def display_students(student_list):
    """Format and display student information."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        ) 

# Read student data from JSON file
with open('Student.json', 'r') as file:
    students = json.load(file)

# Display original student list
print("\nOriginal Student List:")
display_students(students)

# Add user student values
new_student = {
    "F_Name": "Roxanne",
    "L_Name": "Buenaventura",
    "Student_ID": "123456",
    "Email": "roxannebuen@icloud.com"
}

# Append new student to the list
students.append(new_student)

# Display updated student list
print("\nUpdated Student List:")
display_students(students)

# Update list to JSON file
with open('Student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nstudent.json has been updated with the new student information.")


