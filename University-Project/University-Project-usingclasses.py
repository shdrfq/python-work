# Base class for all humans in the university
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Class for Teacher inheriting from Human
class Teacher(Human):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}, Age: {self.age}"

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# Class for Student inheriting from Human
class Student(Human):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.sections = []  # List to store enrolled sections

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}, Age: {self.age}"

    def enroll(self, section):
        self.sections.append(section)
        print(f"{self.name} has enrolled in {section.section_name}.")

# Class for Section
class Section:
    def __init__(self, section_name, teacher, students=None):
        if students is None:
            students = []
        self.section_name = section_name
        self.teacher = teacher
        self.students = students

    def __str__(self):
        return f"Section: {self.section_name}, Taught by: {self.teacher.name}"

    def add_student(self, student):
        self.students.append(student)
        student.enroll(self)

    def list_students(self):
        print(f"Students in section {self.section_name}:")
        for student in self.students:
            print(f"- {student.name}")

# Class for University
class University:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.sections = []

    def __str__(self):
         return f"University: {self.name}"

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"{teacher.name} has joined {self.name} as a teacher.")

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has joined {self.name} as a student.")

    def add_section(self, section):
        self.sections.append(section)
        print(f"Section {section.section_name} has been added to {self.name}.")

    def list_teachers(self):
        print(f"Teachers at {self.name}:")
        for teacher in self.teachers:
            print(f"- {teacher}")

    def list_students(self):
        print(f"Students at {self.name}:")
        for student in self.students:
            print(f"- {student}")

# Example Usage:

# Create a university
university = University("PIAIC University")
print(f"="*40)
# Create teachers
teacher_1 = Teacher("Dr. Aysha", 40, "Female", "Mathematics")
teacher_2 = Teacher("Mr. Imran", 35, "Male", "Physics")
teacher_3 = Teacher("Dr. Nadeem Faisal", 44, "Male", "IT")

# Add teachers to the university
print(f"-"*20 +'Add teachers to the university'+"-"*20)
university.add_teacher(teacher_1)
university.add_teacher(teacher_2)
university.add_teacher(teacher_3)

# Create students
student_1 = Student("Sami Ullah", 20, "Male", "S123")
student_2 = Student("Saima Mustafa", 19, "Female", "S124")
student_3 = Student("Shahid Rafiq", 21, "Male", "S125")
student_4 = Student("Saleh Saqib", 21, "Male", "S126")

# Add students to the university
print(f"-"*20 +'Add students to the university'+"-"*20)
university.add_student(student_1)
university.add_student(student_2)
university.add_student(student_3)
university.add_student(student_4)
# Create sections and assign teachers
section_1 = Section("Math 101", teacher_1)
section_2 = Section("Physics 102", teacher_2)
section_3 = Section("IT 103", teacher_3)

# Add sections to the university
print(f"-"*20 +'Add Section to the university'+"-"*20)
university.add_section(section_1)
university.add_section(section_2)
university.add_section(section_3)

# Enroll students in sections
print(f"-"*20 +'Enroll students in sections'+"-"*20)
section_1.add_student(student_1)
section_2.add_student(student_2)
section_3.add_student(student_3)
section_3.add_student(student_4)
# List university teachers and students
print(f"-"*20 +' List university teachers and students'+"-"*20)
university.list_teachers()
university.list_students()

# List students in each section
print(f"-"*20 +' List students in each section'+"-"*20)
section_1.list_students()
section_2.list_students()
section_3.list_students()

# Teacher actions
print(f"-"*20 +' Teacher actions'+"-"*20)
teacher_1.teach()
teacher_2.teach()
teacher_3.teach()

