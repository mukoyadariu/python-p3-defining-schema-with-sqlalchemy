from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

# Creating the database engine and connecting to it
DATABASE_URI = 'sqlite:///students.db'
engine = create_engine(DATABASE_URI, echo=True)  # Set echo to True for debugging

# Creating the table in the database
Base.metadata.create_all(engine)

# Creating a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Adding a student to the database
    new_student = Student(first_name='John', last_name='Doe', age=20)
    session.add(new_student)
    session.commit()

    # Querying and printing all students
    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.first_name} {student.last_name}, Age: {student.age}")

    # Querying and printing a specific student
    specific_student = session.query(Student).filter_by(first_name='John').first()
    if specific_student:
        print(f"Specific Student: {specific_student.first_name} {specific_student.last_name}, Age: {specific_student.age}")
    else:
        print("Specific student not found")

    # Updating a student's age
    if specific_student:
        specific_student.age = 21
        session.commit()
        print("Student's age updated")

    # Deleting a student
    student_to_delete = session.query(Student).filter_by(first_name='John').first()
    if student_to_delete:
        session.delete(student_to_delete)
        session.commit()
        print("Student deleted")

    session.close()
