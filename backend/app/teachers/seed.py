import psycopg
import random
import uuid
from datetime import datetime, timedelta

# Establishing the connection
conn = psycopg.connect(
    dbname="bahaha",  # Replace with your database name
    user="postgres",  # Replace with your database user
    password="12345678",  # Replace with your database password
    host="localhost",  # Replace with your host if needed
    port="5432",  # Default PostgreSQL port
)

# Creating a cursor object
cur = conn.cursor()


# Function to generate random teacher data
def generate_random_teacher(_):
    name = f"Teacher {random.randint(1, 1000)}"
    email = f"teacher{_}@example.com"
    password = f"password{random.randint(1000, 9999)}"
    phone = f"1234567890{random.randint(0, 9)}"
    date_of_birth = datetime.now() - timedelta(
        days=random.randint(6570, 10950)
    )  # Random DOB in the past 18-30 years
    subject = f"Subject {random.choice(['Math', 'Science', 'History', 'Geography', 'English'])}"
    department = f"Department {random.choice(['Science', 'Arts', 'Commerce'])}"
    joining_date = datetime.now() - timedelta(
        days=random.randint(365, 365 * 5)
    )  # Joining within the past 1-5 years
    address = f"Address {random.randint(1, 1000)}"
    teacher_id = str(uuid.uuid4())  # Random UUID for teacher ID

    return (
        name,
        email,
        password,
        phone,
        date_of_birth,
        subject,
        department,
        joining_date,
        address,
        teacher_id,
        datetime.now(),
        datetime.now(),
    )


# Inserting 100 random teacher records
for _ in range(100):
    teacher_data = generate_random_teacher(str(_))
    cur.execute(
        """
        INSERT INTO public.teachers (
            name, email, password, phone, date_of_birth, subject, department, joining_date, address, id, created_at, updated_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """,
        teacher_data,
    )

# Committing the transaction
conn.commit()

# Closing the cursor and connection
cur.close()
conn.close()

print("100 random teachers have been inserted successfully!")
