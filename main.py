import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def connect_to_db(): # Connect to the PostgreSQL database
    connection = psycopg2.connect( # use the config file to connect to the database
        host=config['postgresql']['host'],
        dbname=config['postgresql']['dbname'],
        user=config['postgresql']['user'],
        password=config['postgresql']['password'],
        port=int(config['postgresql']['port'])
    )
    return connection

def getAllStudents():
    database = connect_to_db()
    with database.cursor() as cursor: # create a cursor object using the cursor() method
        cursor.execute("SELECT * FROM students;") # execute the SQL query
        records = cursor.fetchall() # fetch all of the results from the query
        for record in records:
            print(record)
    database.close()

def addStudent(first_name, last_name, email, enrollment_date): # Add a new student to the students table
    database = connect_to_db()
    with database.cursor() as cursor: # create a cursor object using the cursor() method
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",  # execute the SQL query
                    (first_name, last_name, email, enrollment_date))
        database.commit() # commit the transaction
    database.close()

def updateStudentEmail(student_id, new_email): # Update the email of a student
    database = connect_to_db()
    with database.cursor() as cursor: # create a cursor object using the cursor() method
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;",  # execute the SQL query
                    (new_email, student_id))
        database.commit() # commit the transaction
    database.close()

def deleteStudent(student_id): # Delete a student from the students table
    database = connect_to_db()
    with database.cursor() as cursor: # create a cursor object using the cursor() method
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,)) # execute the SQL query
        database.commit() # commit the transaction
    database.close()

getAllStudents()

print("Adding a new student")
addStudent('Chris', 'Rusu', 'ChrisRusu@Carleton.com', '2024-03-018')
getAllStudents()

print("Updating the email of student with id 1")
updateStudentEmail(1, 'newjohn.doe@example.com')
getAllStudents()

print("Deleting the student with id 2")
deleteStudent(2)
getAllStudents()
