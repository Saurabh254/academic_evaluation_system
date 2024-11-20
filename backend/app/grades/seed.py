import psycopg
import random
import json
from datetime import datetime

# Establish a connection to the PostgreSQL database
conn = psycopg.connect(
    dbname="bahaha",  # Replace with your database name
    user="postgres",  # Replace with your database user
    password="12345678",  # Replace with your database password
    host="localhost",  # Replace with your host if needed
    port="5432",  # Default PostgreSQL port
)

# Create a cursor object to interact with the database
cur = conn.cursor()


# Function to retrieve all student IDs from the students table
def get_student_ids():
    cur.execute("SELECT id FROM students;")
    return cur.fetchall()


# Function to generate random grades (mock data for this example)
def generate_random_grade_data(student_id):
    subjects = ["Math", "Science", "History", "English", "Art"]
    subject_grades = {
        subject: random.choice(["A", "B", "B+", "C", "C+"]) for subject in subjects
    }
    cgpa = round(random.uniform(6.0, 10.0), 2)  # CGPA between 6.0 and 10.0
    semester = random.randint(1, 8)  # Random semester between 1 and 8

    return {
        "student_id": student_id,
        "subject": json.dumps(subject_grades),  # Store subject grades as JSON
        "cgpa": cgpa,
        "semester": semester,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }


# Function to insert grade data into the student_grades table
def insert_grade_data(grade_data):
    query = """
    INSERT INTO student_grades (student_id, subject, cgpa, semester, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cur.execute(
        query,
        (
            grade_data["student_id"],
            grade_data["subject"],
            grade_data["cgpa"],
            grade_data["semester"],
            grade_data["created_at"],
            grade_data["updated_at"],
        ),
    )


# Main logic to fetch student IDs and insert grade data
student_ids = get_student_ids()

for student_id_tuple in student_ids:
    student_id = student_id_tuple[0]  # Extract student ID from the tuple
    grade_data = generate_random_grade_data(student_id)
    insert_grade_data(grade_data)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Grade data for students has been inserted successfully!")
