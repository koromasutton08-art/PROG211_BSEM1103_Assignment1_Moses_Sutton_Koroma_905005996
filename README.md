Student Learning Portal / Digital Exam & Results Management System

Course: PROG211 – Object-Oriented Programming 1
Project domain: Education
Language: Python 3

1. Project Overview

The Student Learning Portal / Digital Exam & Results Management System is a console-based Python project created to demonstrate fundamental Object-Oriented Programming (OOP) concepts.

The program models students and examinations, records examination scores, calculates averages, assigns letter grades, displays student records, and searches for a student by ID.

This is an educational prototype. It uses fictional sample data and is not connected to a live university database.

2. Features

• Defines Student and Exam classes.
• Demonstrates attributes, objects, and methods.
• Records examination results and validates scores from 0 to 100.
• Calculates a student’s average score.
• Converts numerical scores into letter grades.
• Stores 10 student objects in a Python list.
• Uses a loop to display all students.
• Searches for a student using their student ID.
• Demonstrates an instance method and a class method (@classmethod).
• Demonstrates interaction between Exam and Student objects.

3. Project Structure

```text
prog211-student-results-system/
├── main.py
├── README.md
├── sample_output.txt
├── PROG211_Student_Results_System_Report.docx
└── .gitignore
```

Include the report and sample_output.txt in the repository if your lecturer expects them. If you use a different folder structure, update this section to match it.

4. Requirements

• Python 3.8 or later is recommended.
• No external Python packages are required.

Check your Python installation:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

5. How to Run the Program

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python main.py
```

If your system uses python3, run:

```bash
python3 main.py
```

6. Classes and Methods

Student

The Student class represents a student.

Attributes

• student_id — the student’s ID.
• name — the student’s name.
• programme — the student’s programme of study.
• results — a dictionary containing course codes and scores.

Methods

• add_result(course_code, score) — validates and stores a result.
• calculate_average() — calculates the average of recorded scores.
• get_grade(score) — returns a letter grade for a score.
• display_profile() — displays the student’s details and results.
• from_string(student_data) — a class method that creates a student object from comma-separated data.

Example:

```python
student = Student.from_string(
    "SL001,Mohamed Kamara,Software Engineering"
)
```

Exam

The Exam class represents an examination or course assessment.

Attributes

• course_code — the course code.
• course_name — the course name.
• maximum_score — the maximum permitted score.

Methods

• record_result(student, score) — validates a score and records it for a Student object.
• display_exam() — displays the examination details.

7. OOP Concepts Demonstrated

• Classes and objects: Student and Exam define the structure and behaviour of objects.
• Attributes: Store student, course, and result information.
• Instance methods: Operate on individual objects, for example calculate_average().
• Class method: Student.from_string() creates a student object through the class.
• Object interaction: An Exam object records a result for a Student object.
• Data validation: The program rejects scores outside the permitted range.

8. Data Structure and Search

The program uses a Python list named students to store ten Student objects. A for loop displays the list. The search_student() function searches for a matching student ID and returns the corresponding object, or None if no match is found.

The example searches for student ID SL007.

9. Sample Output

The program displays examination information, student profiles, the list of students, a search result, a class-method demonstration, and a system summary.

Example:

```text
===== EXAM INFORMATION =====
PROG211 - Object-Oriented Programming 1 (Maximum: 100)
DBS201 - Database Systems (Maximum: 100)

===== ALL REGISTERED STUDENTS =====
SL001 | Mohamed Kamara | Software Engineering
SL002 | Fatmata Sesay | Information Technology
SL003 | Abdul Sesay | Software Engineering
...
SL010 | Kadiatu Bah | Information Technology

===== SEARCH RESULT =====
Student with ID SL007 found:
```

Run python main.py to see the complete output.

10. Digital Public Goods (DPG) Considerations

• Openness and reuse: The source code can be shared and extended for learning or further development.
• Privacy: The sample records are fictional. A real student system should implement authentication, authorization, secure storage, and appropriate data-access controls.
• Accessibility: The console uses readable text and does not rely on colour alone to communicate information.
• Interoperability: The prototype uses standard Python structures and can be adapted to work with a database in the future.
• Documentation: This README explains the project purpose, requirements, design, and execution steps.

These are design considerations for the educational prototype, not a claim that the project has been formally certified as a Digital Public Good.

11. Limitations and Future Improvements

• Data is held in memory and is lost when the program closes.
• The program uses sample records rather than interactive user input.
• It does not include user accounts or role-based permissions.
• A future version could use SQLite or MySQL for persistent storage.
• Automated tests and a graphical user interface could be added.

12. Uploading the Project to GitHub

Create a new repository on GitHub, for example:

prog211-student-results-system

Open a terminal in your project folder and run:

```bash
git init
git add .
git commit -m "Initial PROG211 student results system"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```



13. Academic Note

This project is intended as a learning demonstration for PROG211. Make sure you understand the classes, attributes, methods, data structure, search operation, and DPG considerations so you can explain your implementation during assessment.
