# Roxanne Buenaventura
# 10 May 2026
# CSD 205 Assignment 9.2
# This program will collect grade information from a user and calculate their gpa.

# Create class
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
# Add course information to course list
    def add_course(self, course_name, credits, grade):
        self.courses.append({
            "course_name": course_name,
            "credits": credits,
            "grade_points": grade
        })
# Calculate gpa by dividing total grade points by total credits
    def calc_gpa(self):
        total_credits = 0
        total_grade_points = 0

        for course in self.courses:
            total_credits += course["credits"]
            total_grade_points += course["credits"] * course["grade_points"]

        if total_credits == 0:
            return 0

        return total_grade_points / total_credits
# Format and print student information, courses, and gpa
    def print_student_info(self):
        print("-" * 50)
        print(f"Student Name: {self.first_name} {self.last_name}")
        print("-" * 50)
        print("Courses:")
        for course in self.courses:
            print(f"{course['course_name']} - Credits: {course['credits']}, Grade Points: {course['grade_points']}")
        print(f"GPA: {self.calc_gpa():.2f}")

# Main program
student = Student(input("Enter first name: "), input("Enter last name: "))

# Loop to collect course information until user decides to stop adding courses
while True:
    course_name = input("Enter course name: ")
    credits = float(input("Enter number of credits: "))
    grade = float(input("Enter grade points: "))
    student.add_course(course_name, credits, grade)
    continue_adding = input("Do you want to add another course? (yes/no): ")
    if continue_adding.lower() != "yes":
        break
# Print student information, courses, and gpa
student.print_student_info()

