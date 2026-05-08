# Programmers: Samuel Gaines and Javan Graber
# Date: 5/7/26
# Program: Student Info Database Manager

import sqlite3


#Connects the Programs
conn = sqlite3.connect('students_info.db')
cur=conn.cursor()
# section for adding the major
def add_major():

    #Gets the information from the User
    majors_id= input("Enter Majors ID: ")
    majors_name= input("Enter Majors Name: ")

    #Inserts the information given
    cur.execute("INSERT INTO Majors VALUES (?,?)",(majors_id, majors_name))

    conn.commit()

    print("Major Added Successfully")

#section for adding the department

def add_department():
    department_id= input("Enter Department ID: ")
    department_name= input("Enter Department Name: ")

    cur.execute("INSERT INTO DEPARTMENT VALUES (?,?)",(department_id,department_name))

    conn.commit()

    print("Department Added Successfully")

#section for the student

def add_student():
    student_id= input("Enter Student ID: ")
    student_name= input("Enter Student Name: ")
    cur.execute("INSERT INTO STUDENT VALUES (?,?)",(student_id,student_name))
    conn.commit()
    print("Student Added Successfully")

#section for viewing the major
def view_majors():

    cur.execute("SELECT* FROM Majors")

    rows = cur.fetchall()

    print("Majors:")
    for row in rows:
        print(row)

def view_departments():
    cur.execute("SELECT* FROM Department")
    rows = cur.fetchall()
    print("Departments:")
    for row in rows:
        print(row)

def view_student():

    cur.execute("SELECT* FROM Student")
    rows = cur.fetchall()
    print("Students:")
    for row in rows:
        print(row)

def edit_major():

    new_major_id= input("Enter Major ID for updating: ")
    new_major_name= input("Enter Major Name for updating: ")

    cur.execute('UPDATE Majors, SET Major name=? WHERE id=?',(new_major_id,new_major_name))
    conn.commit()

    print("Major Updated Successfully")


def edit_department():
    new_department_id= input("Enter Department ID for updating: ")
    new_department_name= input("Enter Department Name for updating: ")

    cur.execute('UPDATE Department, SET Department_name=? WHERE id=?',(new_department_id,new_department_name))
    conn.commit()
    print("Department Updated Successfully")


def edit_student():
    new_student_id= input("Enter Student ID for updating: ")
    new_student_name= input("Enter Student Name for updating: ")

    cur.execute('UPDATE Student, Set Student_name=? WHERE id=?',(new_student_id,new_student_name))
    conn.commit()
    print("Student Updated Successfully")


def display_menu():

    print("Student Info Database Manager")
    print("1. Add Major")
    print("2. Add Department")
    print("3. Add Student")
    print("4. View Major")
    print("5. View Department")
    print("6. View Student")
    print("7. Edit Major")
    print("8. Edit Department")
    print("9. Edit Student")
    print("10. Exit")

def main():

    choice= 0
    while choice != 10:
        display_menu()
        choice = int(input("Hello, please enter your choice of action: "))

        if choice == 1:
            add_major()

        elif choice == 2:
            add_department()

        elif choice == 3:
            add_student()

        elif choice == 4:
            view_majors()

        elif choice == 5:
            view_departments()

        elif choice == 6:
            view_student()

        elif choice == 7:
            edit_major()

        elif choice == 8:
            edit_department()

        elif choice == 9:
            edit_student()

        elif choice == 10:
            print("Thank you for using the JAINES Student Info Database Manager")
            break
        else:
            print("Please enter a valid choice")
    




main()
conn.close()




