
from student import Student


students = []


def student_exists(name, section):
    for student in students:
        if (
            student.name.strip().lower() == name.strip().lower()
            and student.section.strip().lower() == section.strip().lower()
        ):
            return True

    return False


def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter {subject} grade (0-100): "))

            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid grade. Enter a number between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def is_valid_name(name):
    return bool(name.strip()) and all(
        character.isalpha() or character.isspace()
        for character in name
    )


def is_valid_section(section):
    return (
        len(section) >= 2
        and len(section) <= 3
        and section[:-1].isdigit()
        and section[-1].isalpha()
        and section[-1].isupper()
    )


def add_student():
    while True:
        name = input("Enter student's full name: ").strip()

        if is_valid_name(name):
            break

        print("Invalid name. Please enter letters only.")

    while True:
        section = input("Enter student's section (example: 11B): ").strip()

        if is_valid_section(section):
            break

        print("Invalid section. Please use a format like 10A or 11B.")

    if student_exists(name, section):
        print("This student is already registered in this section.")
        return

    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social_studies = get_valid_grade("Social Studies")
    science = get_valid_grade("Science")

    student = Student(
        name,
        section,
        spanish,
        english,
        social_studies,
        science
    )

    students.append(student)

    print("Student added successfully!")

    print("Student name:", name)
    print("Student section:", section)
    print("Spanish grade:", spanish)
    print("English grade:", english)
    print("Social Studies grade:", social_studies)
    print("Science grade:", science)


def view_students():
    if not students:
        print("No students registered.")
        return

    for student in students:
        print("--------------------")
        print("Name:", student.name)
        print("Section:", student.section)
        print("Spanish:", student.spanish)
        print("English:", student.english)
        print("Social Studies:", student.social_studies)
        print("Science:", student.science)


def calculate_average(student):
    total = (
        student.spanish
        + student.english
        + student.social_studies
        + student.science
    )

    average = total / 4

    return average


def view_top_students():
    if not students:
        print("No students registered.")
        return

    sorted_students = sorted(
        students,
        key=calculate_average,
        reverse=True
    )

    print("===== TOP 3 STUDENTS =====")

    for student in sorted_students[:3]:
        print("Name:", student.name)
        print("Section:", student.section)
        print("Average:", calculate_average(student))
        print("--------------------")


def view_average_grade():
    if not students:
        print("No students registered.")
        return

    total = 0

    for student in students:
        total += calculate_average(student)

    average = total / len(students)

    print("Overall student average:", average)
