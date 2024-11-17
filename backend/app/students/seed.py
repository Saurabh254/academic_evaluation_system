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


# Function to generate random student data
def generate_random_student(_):
    name = f"Student {random.randint(1, 1000)}"
    password = f"password{random.randint(1000, 9999)}"
    phone = f"1234567890{random.randint(0, 9)}"
    active = True
    address = f"Address {random.randint(1, 1000)}"
    email = f"student{random.randint(1, 1000)}@example.com"
    father_name = f"Father {random.randint(1, 1000)}"
    mother_name = f"Mother {random.randint(1, 1000)}"
    dob = datetime.now() - timedelta(
        days=random.randint(6570, 10950)
    )  # Random DOB in the past 18-30 years
    student_id = str(uuid.uuid4())  # Random UUID for student ID
    created_at = datetime.now()
    updated_at = created_at

    return (
        name,
        enrollment,
        password,
        phone,
        active,
        address,
        email,
        father_name,
        mother_name,
        dob,
        student_id,
        created_at,
        updated_at,
    )


# Inserting 100 random student records
for _ in range(100):
    student_data = generate_random_student(str(_))
    cur.execute(
        """
        INSERT INTO public.students (
            name,  password, phone, active, address, email, father_name, mother_name, dob, id, created_at, updated_at
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """,
        student_data,
    )

# Committing the transaction
conn.commit()

# Closing the cursor and connection
cur.close()
conn.close()

print("100 random students have been inserted successfully!")
