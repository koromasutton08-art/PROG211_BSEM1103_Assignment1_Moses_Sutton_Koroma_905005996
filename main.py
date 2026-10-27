class Student:
    school_name = "Limkokwing University of Creative Technology"

    def __init__(self, student_id, name, programme):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.results = {}

    # Instance method
    def add_result(self, course_code, score):
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")

        self.results[course_code] = score

    # Instance method
    def calculate_average(self):
        if not self.results:
            return 0

        return sum(self.results.values()) / len(self.results)

    # Instance method
    def get_grade(self, score):
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 40:
            return "D"
        else:
            return "F"

    # Instance method
    def display_profile(self):
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Programme  :", self.programme)

        if self.results:
            print("Results:")

            for course, score in self.results.items():
                grade = self.get_grade(score)

                print(
                    f"  {course}: {score}% ({grade})"
                )

            print(
                f"Average    : "
                f"{self.calculate_average():.2f}%"
            )
        else:
            print("Results    : No results available.")

    # Class method
    @classmethod
    def from_string(cls, student_data):
        student_id, name, programme = student_data.split(",")

        return cls(
            student_id.strip(),
            name.strip(),
            programme.strip()
        )


class Exam:

    def __init__(
        self,
        course_code,
        course_name,
        maximum_score=100
    ):
        self.course_code = course_code
        self.course_name = course_name
        self.maximum_score = maximum_score

    # Instance method
    def record_result(self, student, score):

        if not isinstance(student, Student):
            raise TypeError(
                "Result must be recorded for a Student object."
            )

        if not 0 <= score <= self.maximum_score:
            raise ValueError(
                f"Score must be between 0 and "
                f"{self.maximum_score}."
            )

        student.add_result(
            self.course_code,
            score
        )

    # Instance method
    def display_exam(self):

        print(
            f"{self.course_code} - "
            f"{self.course_name} "
            f"(Maximum: {self.maximum_score})"
        )


def search_student(students, student_id):

    for student in students:

        if student.student_id == student_id:
            return student

    return None


def display_all_students(students):

    print("\n===== ALL REGISTERED STUDENTS =====")

    for student in students:

        print(
            f"{student.student_id} | "
            f"{student.name} | "
            f"{student.programme}"
        )


def main():

    print("===== EXAM INFORMATION =====")

    # Create students
    student1 = Student.from_string(
        "SL001,Mohamed Kamara,Software Engineering"
    )

    student2 = Student(
        "SL002",
        "Fatmata Sesay",
        "Information Technology"
    )

    # Create exams
    exam_prog = Exam(
        "PROG211",
        "Object-Oriented Programming 1"
    )

    exam_db = Exam(
        "DBS201",
        "Database Systems"
    )

    # Display exams
    exam_prog.display_exam()
    exam_db.display_exam()

    # Student 1 results
    exam_prog.record_result(student1, 82)
    exam_db.record_result(student1, 74)

    # Student 2 results
    exam_prog.record_result(student2, 68)
    exam_db.record_result(student2, 79)

    # Display profiles
    print("\n===== SAMPLE STUDENT PROFILES =====")

    student1.display_profile()

    print()

    student2.display_profile()

    # Create list containing 10 students
    students = [
        student1,
        student2,

        Student(
            "SL003",
            "Abdul Sesay",
            "Software Engineering"
        ),

        Student(
            "SL004",
            "Isatu Kamara",
            "Information Technology"
        ),

        Student(
            "SL005",
            "Alhaji Conteh",
            "Computer Science"
        ),

        Student(
            "SL006",
            "Mariama Bangura",
            "Software Engineering"
        ),

        Student(
            "SL007",
            "Ibrahim Koroma",
            "Information Technology"
        ),

        Student(
            "SL008",
            "Hawa Turay",
            "Computer Science"
        ),

        Student(
            "SL009",
            "Sorie Jalloh",
            "Software Engineering"
        ),

        Student(
            "SL010",
            "Kadiatu Bah",
            "Information Technology"
        )
    ]

    # Scores for the 10 students
    scores = [
        82,
        68,
        75,
        61,
        55,
        73,
        64,
        49,
        88,
        70
    ]

    # Record results
    for student, score in zip(students, scores):

        exam_prog.record_result(
            student,
            score
        )

    # Display all students
    display_all_students(students)

    # Search for a student
    print("\n===== SEARCH RESULT =====")

    search_id = "SL007"

    found_student = search_student(
        students,
        search_id
    )

    if found_student:

        print(
            f"Student with ID {search_id} found:"
        )

        found_student.display_profile()

    else:

        print(
            f"No student found with ID {search_id}."
        )

    # Class method demonstration
    print("\n===== CLASS METHOD DEMONSTRATION =====")

    new_student = Student.from_string(
        "SL011,Josephine Williams,Information Technology"
    )

    print(
        f"Created using @classmethod: "
        f"{new_student.student_id} - "
        f"{new_student.name}"
    )

    # System summary
    print("\n===== SYSTEM SUMMARY =====")

    print(
        f"Total registered students: {len(students)}"
    )

    print("Data structure used: List")

    print(
        "Instance methods demonstrated:"
    )

    print(
        "add_result(), calculate_average(), "
        "get_grade(), display_profile(), "
        "record_result(), display_exam()"
    )

    print(
        "Class method demonstrated: "
        "Student.from_string()"
    )


if __name__ == "__main__":
    main()