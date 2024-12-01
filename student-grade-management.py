grades = []

def view_all_student_grades():
    """
    This function prints out all the student's grades in the list.
    """
    if not grades:
        print("There are no students in the list.\n")
    else:
        print("\nHere are all the students' grades:")
        for i in range(len(grades)):
            print(f"Student {i + 1}: {grades[i]['name']}, {grades[i]['subject']}, {grades[i]['grade']}")
            
def student_grade(name, subject, grade):
    """
    This function takes in a student's name, subject and grade and adds it to the dictionary of
    """
    student = {
        "name": name,
        "subject": subject,
        "grade": grade
    }
    grades.append(student)
    print(f"Student name'{student['name']}, score {student['grade']}, in {student['subject']}' has been added to the list.\n")

def view_specific_student_grades():
    student = input("Enter the student's name: ")
    for i in range(len(grades)):
        if grades[i]['name'] == student:
            print(f"Student {student} has a grade of {grades[i]['grade']} in {grades[i]['subject']}.")
            break
    else:
        print("Student not found.\n")

def delete_student():
    """
    This function deletes a student from the list.
    """
    student = input("Enter the student's name: ")
    for i in range(len(grades)):
        if grades[i]['name'] == student:
            del grades[i]
            print(f"Student {student} has been deleted from the list.\n")
            break
    else:
        print("Student not found.\n")

while True:
    print("\nStudent Grades Menu:")
    print("1. View all student grades")
    print("2. Add a student's grade")
    print("3. View a specific student's grade")
    print("4. Delete a student's grade")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        view_all_student_grades()
    elif choice == '2':
        name = input("Enter the student's name: ")
        subject = input("Enter the subject: ")
        grade = input("Enter the grade: ")
        student_grade(name, subject, grade)
    elif choice == '3':
        view_specific_student_grades()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")