# Programmers: Javan Graber and Samuel Gaines
# Date: 5/7/26
# Program #2: Student Info Database Tables

import sqlite3

def create_student_database_tables():
    conn = sqlite3.connect('students_info.db')
    cur = conn.cursor()
    # Create the Majors table
    cur.execute('''CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY NOT NULL, 
                                                         MajorName TEXT)''')
    # Create the Departments table
    cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DepartmentID INTEGER PRIMARY KEY NOT NULL, 
                                                              DepartmentName TEXT)''')
    # Create the Students table
    cur.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER NOT NULL, 
                                                           StudentName TEXT, 
                                                           StudentAge INTEGER,
                                                           MajorID INTEGER, 
                                                           DepartmentID INTEGER, 
                                                           FOREIGN KEY (MajorID) REFERENCES 
                                                               Majors (MajorID), 
                                                           FOREIGN KEY (DepartmentID) REFERENCES
                                                               Departments (DepartmentID))''')
    conn.commit()
    conn.close()
# Call the function
create_student_database_tables()
