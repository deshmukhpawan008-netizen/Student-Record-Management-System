students = []

def add_student():
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    student = {
        "roll_number": roll_number,
        "name": name,
        "department": department
    }

    students.append(student)
    print("Student added successfully!")


def search_student():
    roll_number = int(input("Enter Roll Number to Search: "))

    for student in students:
        if student["roll_number"] == roll_number:
            print("Student Found!")
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            return

    print("Student not found!")

add_student()
search_student()

def update_student():
    roll_number = int(input("Enter Roll Number to Update: "))

    for student in students:
        if student["roll_number"] == roll_number:
            student["name"] = input("Enter New Name: ")
            student["department"] = input("Enter New Department: ")

            print("Student record updated successfully!")
            return

    print("Student not found!")

def delete_student():
    roll_number = int(input("Enter Roll Number to Delete: "))

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")

def display_students():
    if len(students) == 0:
        print("No student records found!")
        return

    print("\nAll Student Records:")

    for student in students:
        print("--------------------")
        print("Roll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Department:", student["department"])

def count_students():
    print("Total Students:", len(students))

def calculate_average(marks):
    if len(marks) == 0:
        return 0

    total = sum(marks)
    average = total / len(marks)

    return average

def find_highest_scorer(student_marks):
    if len(student_marks) == 0:
        print("No marks available!")
        return

    highest_student = max(student_marks, key=student_marks.get)

    print("Highest Scorer:", highest_student)
    print("Marks:", student_marks[highest_student])

def students_by_department():
    department = input("Enter Department: ")

    found = False

    for student in students:
        if student["department"].lower() == department.lower():
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("--------------------")
            found = True

    if not found:
        print("No students found in this department!") 

def menu():
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Students")
    print("7. Students by Department")
    print("8. Exit")

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_students()

    elif choice == "6":
        count_students()

    elif choice == "7":
        students_by_department()

    elif choice == "8":
        print("Thank you for using Student Record Management System!")
        break

    else:
        print("Invalid choice! Please try again.")