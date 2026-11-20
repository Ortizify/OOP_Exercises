
import csv
from actions import students, student_exists
from student import Student


def export_students():
    if not students:
        print("No students to export.")
        return

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "section",
                "spanish",
                "english",
                "social_studies",
                "science"
            ]
        )

        writer.writeheader()

        for student in students:
            writer.writerow({
                "name": student.name,
                "section": student.section,
                "spanish": student.spanish,
                "english": student.english,
                "social_studies": student.social_studies,
                "science": student.science
            })

    print("Students exported successfully!")


def import_students():
    print("Importing students from CSV...")

    try:
        with open("students.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    float(row["spanish"]),
                    float(row["english"]),
                    float(row["social_studies"]),
                    float(row["science"])
                )

                if not student_exists(student.name, student.section):
                    students.append(student)
                    print("Student imported successfully!")
                else:
                    print("Student already exists. Skipping duplicate.")

    except FileNotFoundError:
        print("No CSV file found. Starting with an empty student list.")
