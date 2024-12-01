grades = []

while True:
    print("\nStudent Grades Menu:")
    print("1. View all student grades")
    print("2. Add a student's grade")
    print("3. View a specific student's grade")
    print("4. Delete a student's grade")
    print("5. Exit")
    
    choice = input("Choose an option (1,2,3,4,5): ")
    
    if choice == "1":
        # This option will print all the student's grades in the list.
        if not grades:
            print("No grades have been added yet.")
        else:
            for student_record in grades:
                print(f"Student {student_record['name']} has a grade of {student_record['grade']} in {student_record['subject']}.")

    elif choice == "2":
        # This option will add a student's grade to the list
        name = input("Enter the student's name: ")
        subject = input("Enter the subject: ")
        
        while True:
            try:
                grade = int(input("Enter the student's grade: "))
                break
            except ValueError:
                print("Please enter a valid integer for the grade.")
        
        student = {"name": name, "subject": subject, "grade": grade}
        grades.append(student)
        print(f"Student '{student['name']}' with a score of {student['grade']} in '{student['subject']}' has been added to the list.\n")

    elif choice == "3":
        # This option will print a specific student's grade in the list.
        student_name = input("Enter the student's name: ")
        found = False
        for student_record in grades:
            if student_record['name'].lower() == student_name.lower():
                print(f"Student {student_record['name']} has a grade of {student_record['grade']} in {student_record['subject']}.")
                found = True
                break
        if not found:
            print(f"Student {student_name} has not been added to the list.")

    elif choice == "4":
        # This option will delete a student's grade from the list.
        student_name = input("Enter the student's name: ")
        found = False
        for i in range(len(grades)):
            if grades[i]['name'].lower() == student_name.lower():
                del grades[i]
                print(f"Student {student_name} has been deleted from the list.\n")
                found = True
                break
        if not found:
            print("Student not found.\n")

    elif choice == "5":
        print("Exiting the program.\n")
        break

    else:
        print("Invalid choice. Please select a valid option.")