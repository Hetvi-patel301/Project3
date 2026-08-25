print("Welcome to the Student Data Organizer!")
print()
students = []
while True:
    print("Select an option:")
    print("1. Add student\n2. Display All students\n3. Update student Information\n4. Delete student\n5. Display Subjects offered\n6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Enter student details:")
            s_id = int(input("Student ID:"))
            id_exists = False
            for i in students:
                if i["Student_info"][0] == s_id:
                    id_exists = True
                    break
            while True:
                if id_exists:
                    print("Student ID already exists. Please enter a unique Student ID.")
                    break
                else:
                    name = input("Name:")
                    age = int(input("Age:"))
                    grade = input("Grade:")
                    birth_date = input("Date of Birth (YYYY-MM-DD):")
                    sub = set(input("Subjects (comma -separeted):").split(","))
                Student_info = (s_id, birth_date)
                s={
                    "Student_info" : Student_info,
                    "Name" : name,
                    "Age" : age,
                    "Grade" : grade,
                    "Subjects":sub
                    }
                students.append(s)
                print("student added successfully!")
                break
        case 2:
            if len (students) == 0:
                print("No student Record Found.")
            else:
                print("--- Display All students ---")
                for i in students:
                    print("student ID:",i["Student_info"][0],
                          "| Name:",i["Name"],
                          "| Age:",i["Age"],
                          "| Grade: ",i["Grade"],
                          "| Subjects:", ", ".join(i["Subjects"]))
        case 3:
            print()
            print("--- Updating Student Information ---")

            var = int(input("Enter Student ID: "))

            found = False

            for i in students:
                if i["Student_info"][0] == var:

                    print("1. Name")
                    print("2. Age")
                    print("3. Grade")
                    print("4. Subjects")

                    update = int(input("What do you want to update? "))

                    if update == 1:
                        i["Name"] = input("Enter new name: ")

                    elif update == 2:
                        i["Age"] = int(input("Enter new age: "))

                    elif update == 3:
                        i["Grade"] = input("Enter new grade: ")


                    elif update == 4:
                        i["Subjects"] = set(input("Enter new subjects: ").split(","))

                    else:
                        print("Invalid choice.")
                        break

                    print("Student information updated successfully!")
                    found = True
                    break

            if found == False:
                print("Student ID not found.")
        case 4:
            print()
            print("--- Delete Student ---")
            var1 = int(input("Enter Student ID: "))
            found = False

            for i in students:
                if i["Student_info"][0] == var1:
                    del students[students.index(i)]
                    print("Student deleted successfully!")
                    found = True
                    break

            if found == False:
                print("Student ID not found.")
        case 5:
            print()
            print("--- Subjects Offered ---")

            if len(students) == 0:
                print("No student record found.")
            else:
                for i in students:
                    print(i["Student_info"][0],":",", ".join(i["Subjects"]))
        case 6:
            print("Thank you for using the Student Data Organizer!")
            break
        case _:
            print("Invalid Choice")