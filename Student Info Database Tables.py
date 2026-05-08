# Programmer: Javan Graber with Samuel Gaines
# Date: 5/8/26
# Program #2: Student Info Database Tables Creation

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
    cur.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY NOT NULL, 
                                                           StudentName TEXT, 
                                                           StudentPhone INTEGER,
                                                           MajorID INTEGER, 
                                                           DepartmentID INTEGER, 
                                                           FOREIGN KEY (MajorID) REFERENCES 
                                                               Majors (MajorID), 
                                                           FOREIGN KEY (DepartmentID) REFERENCES
                                                               Departments (DepartmentID))''')
    conn.commit()
    conn.close()

create_student_database_tables()
