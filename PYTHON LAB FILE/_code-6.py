
students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully.")

def update_marks():
    name = input("Enter student name to update: ")

    if name in students:
        marks = float(input("Enter new marks: "))
        students[name] = marks
        print("Marks updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")

    if name in students:
        del students[name]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def calculate_average():
    if len(students) > 0:
        average = sum(students.values()) / len(students)
        print("Average marks:", round(average, 2))
    else:
        print("No student records available.")

def display_students():
    if students:
        print("\nStudent Records:")
        for name, marks in students.items():
            print(name, ":", marks)
    else:
        print("No student records available.")

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Calculate Average")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        calculate_average()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")