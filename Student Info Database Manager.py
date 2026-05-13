# Programmers: Samuel Gaines and Javan Graber
# Date: 5/13/26
# Program: Student Info Database Manager

import sqlite3

# Section for adding a Major
def add_major():
    conn = None
    print("1. Add Major")
    new_major = input("Enter Major Name: ")
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        cur.execute('''INSERT INTO Majors (MajorName)
                    VALUES (?)''', (new_major,))
        conn.commit()
        # Display changes
        num_added = cur.rowcount
        print(f"{num_added} row(s) added")
    # Prepare for exceptions
    except sqlite3.Error as err:
        print("Database Error", err)
    except:
        print("Error has occurred. Make sure you enter valid information!")
    finally:
        if conn is not None:
            conn.close()

# Section for adding a Department
def add_department():
    conn = None
    print("2. Add Department")
    new_department = input("Enter Department Name: ")
    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        cur.execute('''INSERT INTO Departments (DepartmentName)
                    VALUES (?)''', (new_department,))
        conn.commit()
        # Display changes
        num_added = cur.rowcount
        print(f"{num_added} row(s) added")
    # Prepare for exceptions
    except sqlite3.Error as err:
        print("Database Error", err)
    except:
        print("Error has occurred. Make sure you enter valid information!")
    finally:
        if conn is not None:
            conn.close()

# Section for adding a Student
def add_student():
    print("3. Add Student")
    conn = None
    new_student_name = input("Enter the name of the new Student: ")
    new_student_phone = input("Enter the phone number of the new Student: ")
    new_student_major = input("Enter the Major for the new Student (It must be an already existing): ")
    new_student_department = input("Enter the Department for the new Student (It must be already existing): ")

    try:
        conn = sqlite3.connect("students_info.db")
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        # Get all Major names and Department names
        cur.execute('SELECT MajorName FROM Majors')
        major_results = cur.fetchall()
        cur.execute('SELECT DepartmentName FROM Departments')
        department_results = cur.fetchall()
        found_major = 0
        found_department = 0
        # Search to see if the Major and Department exist in their respective tables
        for row in major_results:
            if new_student_major == row[0]:
                found_major = 1
        for row in department_results:
            if new_student_department == row[0]:
                found_department = 1
        if found_major == 0:
            print("That Major does not exist yet (or you spelled it wrong or without capitals). You will have to create it first.")
        # If the Major does exist, get the ID that references it and insert it in a list
        elif found_major == 1:
            cur.execute('SELECT MajorID FROM Majors WHERE lower(MajorName)=?',
                        (new_student_major.lower(),))
            retrieved_major_id = cur.fetchone()
            major_id_list = []
            for value in retrieved_major_id:
                major_id_list.append(value)
            # Create a variable that references it
            major_id = major_id_list[0]
            if found_department == 0:
                print("That Department does not exist yet (or you spelled it wrong or without capitals). You will have to create it first.")
            # If the Department does exist, get the ID that references it and insert it in a list
            elif found_department == 1:
                cur.execute('SELECT DepartmentID FROM Departments WHERE lower(DepartmentName)=?',
                            (new_student_department.lower(),))
                retrieved_department_id = cur.fetchone()
                department_id_list = []
                for value in retrieved_department_id:
                    department_id_list.append(value)
                # Create a variable that references the ID
                department_id = department_id_list[0]
                # Insert the values into the Students table
                cur.execute('''INSERT INTO Students (StudentName, StudentPhone, MajorID, DepartmentID)
                                VALUES (?, ?, ?, ?)''',
                            (new_student_name, new_student_phone, major_id, department_id))
        conn.commit()
        # Display changes
        num_added = cur.rowcount
        if num_added == 1:
            print(f"{num_added} row(s) added")
    # Prepare for exceptions
    except sqlite3.Error as err:
        print("Database Error", err)
    except:
        print("Error has occurred. Make sure you enter valid information!")
    finally:
        if conn is not None:
            conn.close()

# Section for viewing a Major
def view_major():
    print("4. View Major")
    conn = None
    major_name = input("Enter the name of the Major to search for: ")
    # Prepare for exceptions
    try:
        conn = sqlite3.connect('students_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT MajorName FROM Majors 
                           WHERE lower(MajorName) ==?''',
                    (major_name.lower(),))
        results = cur.fetchall()
        # Find the length to show results
        length = len(results)
        print(f"{length} row(s) found")
        # Print each row
        for row in results:
            print(f"Major Name: {row[0]:6}")
    # Prepare for exceptions
    except sqlite3.Error as err:
        print("Database Error", err)
    except:
        print("Error has occurred. Make sure you enter valid information!")

    finally:
        if conn is not None:
            conn.close()

# Section for viewing a Department
def view_department():
    print("5. View Department")
    conn = None
    department_name = input("Enter the name of the Department to search for: ")
    # Prepare for exceptions
    try:
        conn = sqlite3.connect('students_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        cur.execute('''SELECT DepartmentName FROM Departments 
                           WHERE lower(DepartmentName) ==?''',
                    (department_name.lower(),))
        # Get the result to display if it is found
        results = cur.fetchall()
        length = len(results)
        print(f"{length} row(s) found")
        # Print the information
        for row in results:
            print(f"Department Name: {row[0]:6}")

    except sqlite3.Error as err:
        print("Database Error", err)
    except:
        print("Error has occurred. Make sure you enter valid information!")
    finally:
        if conn is not None:
            conn.close()

# Section for viewing a Student
def view_student():
    print("6. View Student")
    conn = None
    student_name = input("Enter the name of the Student to search for: ")
    try:
        conn = sqlite3.connect('students_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys = ON')
        # Get the information from that Student, show if it was found, and insert it in a list
        cur.execute('''SELECT StudentName, StudentPhone, MajorID, DepartmentID FROM Students 
                               WHERE lower(StudentName) ==?''',
                    (student_name.lower(),))
        retrieved_student = cur.fetchall()
        # Display the row(s) found and only continue if a result is found
        length = len(retrieved_student)
        print(f"{length} row(s) found")
        if length != 0:
            retrieved_student_list = []
            for value in retrieved_student:
                retrieved_student_list.append(value)
            student_info = retrieved_student_list[0]
            # Establish the Student name and phone number
            student_name = student_info[0]
            student_phone = student_info[1]
            # Establish the Major ID and get the name for the Major it references by inserting it in a list
            major_id = student_info[2]
            cur.execute('SELECT MajorName FROM Majors WHERE MajorID=?', (major_id,))
            retrieved_major_name = cur.fetchone()
            retrieved_major_name_list = []
            for value in retrieved_major_name:
                retrieved_major_name_list.append(value)
            major_name = retrieved_major_name_list[0]
            # Establish the Department ID and get the name for the Department it references by inserting it in a list
            department_id = student_info[3]
            cur.execute('SELECT DepartmentName FROM Departments WHERE DepartmentID=?',
                        (department_id,))
            retrieved_department_name = cur.fetchone()
            retrieved_department_name_list = []
            for value in retrieved_department_name:
                retrieved_department_name_list.append(value)
            department_name = retrieved_department_name_list[0]

            # Print all the information
            print(f"Student Name: {student_name}   Phone: {student_phone}   "
                  f" Major: {major_name} (#ID: {major_id})   Department: {department_name} (#ID: {department_id})")
    # Prepare for any exceptions
    except sqlite3.Error as err:
        print("Database Error", err)
    except:
        print("Error has occurred. Make sure you enter valid information!")

    finally:
        if conn is not None:
            conn.close()

# Section for editing a Major
def edit_major():
    print("7. Edit Major")
    conn = None
    # Call the read function to help the user ensure the existence of the Major
    print("Let's first make sure your Major exists by finding it")
    view_major()
    selected_major = input("Enter the name of the Major you want to edit (or type n to stop): ")
    if selected_major != 'n' and 'N':
        major_change = input("Enter the new Major title: ")

        # Prepare for any exceptions
        try:
            conn = sqlite3.connect('students_info.db')
            cur = conn.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute('''UPDATE Majors 
                                   SET MajorName=? 
                                   WHERE lower(MajorName)==?''',
                        (major_change, selected_major.lower()))
            conn.commit()
            # Get the rows to display the update
            num_edited = cur.rowcount
            print(f"{num_edited} row(s) edited")
        except sqlite3.Error as err:
            print("Database Error", err)
        except:
            print("Error has occurred. Make sure you enter valid information!")
        finally:
            if conn is not None:
                conn.close()

# Section for editing a Department
def edit_department():
    print("8. Edit Department")
    conn = None
    # Call the read function to help the user ensure the existence of the Department
    print("Let's first make sure your Department exists by finding it")
    view_department()
    selected_department = input("Enter the name of the Department you want to edit (or type n to stop): ")
    if selected_department != 'n' and 'N':
        department_change = input("Enter the new Department title: ")

        # Prepare for any exceptions
        try:
            conn = sqlite3.connect('students_info.db')
            cur = conn.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute('''UPDATE Departments 
                                   SET DepartmentName=? 
                                   WHERE lower(DepartmentName)==?''',
                        (department_change, selected_department.lower()))
            conn.commit()
            # Prepare to display an update
            num_edited = cur.rowcount
            print(f"{num_edited} row(s) edited")
        except sqlite3.Error as err:
            print("Database Error", err)
        except:
            print("Error has occurred. Make sure you enter valid information!")
        finally:
            if conn is not None:
                conn.close()

# Section for editing a Student
def edit_student():
    conn = None
    print("9. Edit Student")
    # Call the read function to ensure the Student exists
    print("Let's first make sure your Student exists by finding the Student")
    view_student()
    student_to_update = input("Enter the Student you want to edit (or type n to stop): ")
    if student_to_update != 'n' and 'N':
        # Display the possible options to update
        print("1. Change Name")
        print("2. Change Phone")
        print("3. Change Major")
        print("4. Change Department")
        try:
            selection = int(input("Enter your selection (the number): "))
            # Ensure it is valid
            while selection < 1 or selection > 4:
                print("Invalid selection")
                selection = int(input("Enter your selection: "))
            # Change the name
            if selection == 1:
                new_name = input("Enter the new name: ")
                conn = sqlite3.connect('students_info.db')
                cur = conn.cursor()
                cur.execute("Pragma foreign_keys = ON")
                cur.execute('''UPDATE Students
                                       SET StudentName=?
                                       WHERE lower(StudentName)==?''',
                            (new_name, student_to_update.lower()))
                num_edited = cur.rowcount
                print(f"{num_edited} row(s) edited")
            # Change the phone number
            elif selection == 2:
                new_phone = input("Enter the new phone: ")
                conn = sqlite3.connect('students_info.db')
                cur = conn.cursor()
                cur.execute("Pragma foreign_keys = ON")
                cur.execute('''UPDATE Students
                                           SET StudentPhone=?
                                           WHERE lower(StudentName)==?''',
                            (new_phone, student_to_update.lower()))
                num_edited = cur.rowcount
                print(f"{num_edited} row(s) edited")
            # Change the Major
            elif selection == 3:
                conn = sqlite3.connect('students_info.db')
                cur = conn.cursor()
                cur.execute("Pragma foreign_keys = ON")
                cur.execute('SELECT MajorName FROM Majors')
                # Display the Major options to help the user
                retrieved_major_names = cur.fetchall()
                major_names_list = []
                for value in retrieved_major_names:
                    major_names_list.append(value[0])
                print(f"Here are the Major options: ")
                for value in major_names_list:
                    print(f"Major Name: {value}")
                major_choice = input("What is the new Major for this Student?: ")
                # If the new Major exists, get the ID and change the Student Major to the new one
                if major_choice in major_names_list:
                    cur.execute('SELECT MajorID FROM Majors WHERE lower(MajorName)==?''',
                                (major_choice.lower(),))
                    retrieved_major_id = cur.fetchone()
                    major_id_list = []
                    for value in retrieved_major_id:
                        major_id_list.append(value)
                    major_id = major_id_list[0]
                    cur.execute('''UPDATE Students
                                        SET MajorID=?
                                        WHERE lower(StudentName)==?''',
                                (major_id, student_to_update.lower()))
                    num_edited = cur.rowcount
                    print(f"{num_edited} row(s) edited")
                # Prepare for problems
                else:
                    print("That Major does not exist yet. You will have to create it first.")
                    print("Make sure spelled the Major EXACTLY the same (do not forget capitals)")
            # Change the Department
            elif selection == 4:
                conn = sqlite3.connect('students_info.db')
                cur = conn.cursor()
                cur.execute("Pragma foreign_keys = ON")
                # Get and display the Department options to help the user
                cur.execute('SELECT DepartmentName FROM Departments')
                retrieved_department_names = cur.fetchall()
                department_names_list = []
                for value in retrieved_department_names:
                    department_names_list.append(value[0])
                print(f"Here are the Department options: ")
                for value in department_names_list:
                    print(f"Department Name: {value}")

                department_choice = input("What is the new Department for this Student?: ")
                # If the new Department exists, get the ID and update the Student's Department
                if department_choice in department_names_list:
                    cur.execute('SELECT DepartmentID FROM Departments WHERE lower(DepartmentName)==?''',
                                (department_choice.lower(),))
                    # Get the new department in a list to isolate it
                    retrieved_department_id = cur.fetchone()
                    department_id_list = []
                    for value in retrieved_department_id:
                        department_id_list.append(value)
                    department_id = department_id_list[0]
                    cur.execute('''UPDATE Students
                                    SET DepartmentID=?
                                    WHERE lower(StudentName)==?''',
                                (department_id, student_to_update.lower()))
                    num_edited = cur.rowcount
                    print(f"{num_edited} row(s) edited")
                # Prepare for a problem
                else:
                    print("That Department does not exist yet. You will have to create it first.")
                    print("Make sure spelled the Department EXACTLY the same (do not forget capitals)")
            conn.commit()
        # Prepare for exceptions
        except sqlite3.Error as err:
            print("Database Error", err)
        except:
            print("Error has occurred. Make sure you enter valid information!")

        finally:
            if conn is not None:
                conn.close()

# Section for deleting a Major
def delete_major():
    print("10. Delete Major")
    conn = None
    # Call the read function to ensure the existence of the Major
    print("Let's first make sure your Major exists by finding the Major")
    view_major()
    selected_major = input("Enter the name of the Major you want to delete (or type n and type n again "
                           "for the next question): ")
    sure = input("Are you sure you want to delete this Major? (y/n): ")
    if sure == "y" or sure == "Y":
        # Prepare for an exception
        try:
            conn = sqlite3.connect('students_info.db')
            cur = conn.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute('SELECT MajorID FROM Students')
            # Get the MajorIDs from the Student table and insert them into a list
            retrieved_major_ids = cur.fetchall()
            major_id_list = []
            for value in retrieved_major_ids:
                major_id_list.append(value[0])
            cur.execute('SELECT MajorID FROM Majors WHERE lower(MajorName)=?',
                        (selected_major.lower(),))
            # Get the MajorID from the selected Major and insert it into a list
            retrieved_major_id = cur.fetchone()
            retrieved_major_id_list = []
            for value in retrieved_major_id:
                retrieved_major_id_list.append(value)
            # Isolate the value
            selection_major_id = retrieved_major_id_list[0]
            # Check to see if the selected Major is currently used by a Student. If not, delete it.
            if selection_major_id in major_id_list:
                print("You cannot delete this Major because a Student is currently in it!"
                      " You must change the Student or delete the Student first.")
            elif selection_major_id not in major_id_list:
                cur.execute('''DELETE FROM Majors
                        Where lower(MajorName)=?''',
                        (selected_major.lower(),))
                num_deleted = cur.rowcount
                print(f"{num_deleted} row(s) deleted")
            conn.commit()
        except sqlite3.Error as err:
            print("Database Error", err)
        except:
            print("Error has occurred. Perhaps make sure that the Major to delete is spelled correctly")
        finally:
            if conn is not None:
                conn.close()

# Section for deleting a Department
def delete_department():
    print("11. Delete Department")
    conn = None
    # Call the read function to ensure the existence of the Department
    print("Let's first make sure your Department exists by finding the Department")
    view_department()
    selected_department = input("Enter the name of the Department you want to delete (or type n and"
                                " type n again for the next question): ")
    sure = input("Are you sure you want to delete this Department? (y/n): ")
    if sure == "y" or sure == "Y":
        try:
            conn = sqlite3.connect('students_info.db')
            cur = conn.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            # Get the ID results from the Student table and insert them into a list
            cur.execute('SELECT DepartmentID FROM Students')
            retrieved_department_ids = cur.fetchall()
            department_id_list = []
            for value in retrieved_department_ids:
                department_id_list.append(value[0])
            # Get the Department ID for the selection and insert it into a list
            cur.execute('SELECT DepartmentID FROM Departments WHERE lower(DepartmentName)=?',
                        (selected_department.lower(),))
            retrieved_department_id = cur.fetchone()
            retrieved_department_id_list = []
            for value in retrieved_department_id:
                retrieved_department_id_list.append(value)
            # Make a value reference the value in the Department ID list
            selection_department_id = retrieved_department_id_list[0]
            # Check to see if the Department ID exists in the Students table. If it does not, delete it.
            if selection_department_id in department_id_list:
                print("You cannot delete this Department because a Student is currently in it!"
                      " You must change the Student or delete the Student first.")
            elif selection_department_id not in department_id_list:
                cur.execute('''DELETE FROM Departments
                        Where lower(DepartmentName)=?''',
                        (selected_department.lower(),))
                # Display the change
                num_deleted = cur.rowcount
                print(f"{num_deleted} row(s) deleted")
            conn.commit()
        # Prepare for an exception
        except sqlite3.Error as err:
            print("Database Error", err)
        except:
            print("Error has occurred. Perhaps make sure that the Department to delete is spelled correctly")
        finally:
            if conn is not None:
                conn.close()

# Section for deleting a Student
def delete_student():
    conn = None
    print("12. Delete Student")
    # Call the read function to ensure the existence of the Student
    print("Let's first make sure your Student exists by finding the Student")
    view_student()
    selected_student = input("Enter the name of the Student you want to delete (or type n and "
                             "type n again for the next question): ")
    sure = input("Are you sure you want to delete this Student? (y/n): ")
    if sure == "y" or sure == "Y":
        # Delete the Student
        try:
            conn = sqlite3.connect('students_info.db')
            cur = conn.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute('''DELETE FROM Students
                            Where lower(StudentName)=?''',
                        (selected_student.lower(),))
            conn.commit()
            # If a change was made, display it
            num_deleted = cur.rowcount
            print(f"{num_deleted} row(s) deleted")
        # Prepare for exceptions
        except sqlite3.Error as err:
            print("Database Error", err)
        except:
            print("Error has occurred. Make sure you enter valid information!")
        finally:
            if conn is not None:
                conn.close()



# Section for displaying the menu
def display_menu():
    print("Student Info Database Manager")
    print("-------------------")
    print("1. Add Major")
    print("2. Add Department")
    print("3. Add Student")
    print("-------------------")
    print("4. View Major")
    print("5. View Department")
    print("6. View Student")
    print("-------------------")
    print("7. Edit Major")
    print("8. Edit Department")
    print("9. Edit Student")
    print("-------------------")
    print("10. Delete Major")
    print("11. Delete Department")
    print("12. Delete Student")
    print("-------------------")
    print("13. Exit")

# Section for getting the choice and calling the required function
def main():
    choice = 0
    while choice != 13:
        # Display the options
        display_menu()

        try:
            choice = int(input("Hello, please enter your choice of action (the number): "))
        except ValueError:
            print("Sorry, your choice of action was invalid (it must be a valid NUMBER)")


        if choice == 1:
            add_major()

        elif choice == 2:
            add_department()

        elif choice == 3:
            add_student()

        elif choice == 4:
            view_major()

        elif choice == 5:
            view_department()

        elif choice == 6:
            view_student()

        elif choice == 7:
            edit_major()

        elif choice == 8:
            edit_department()

        elif choice == 9:
            edit_student()

        elif choice == 10:
            delete_major()

        elif choice == 11:
            delete_department()

        elif choice == 12:
            delete_student()

        elif choice == 13:
            print("Thank you for using the JAINES Student Info Database Manager")

        else:
            print("Please enter a valid choice")

if __name__ == "__main__":
    main()
