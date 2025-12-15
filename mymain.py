
# Task 1.1: Variable Declaration and Data Types
student_name = "Akinlade Sofiu Gbolahan" # string
matric_number = "22/66MB065" # string
age = 22 # integer
cgpa = 4.82 # float
is_active = True # boolean
courses_registered = ["FIN311", "FIN317", "GSE301", "FIN323"] # list of strings
grades = {"FIN311": "A", "FIN317": "A", "GSE301": "A", "FIN323": "A"} # dictionary
score = {"FIN311": "84", "FIN317": "81", "GSE301": "95", "FIN323": "84"} # dictionary

#creating record to store student information
student_record = {
    "student_name": student_name,
    "matric_number": matric_number,
    "age": age,
    "cgpa": cgpa,
    "is_active": is_active,
    "courses_registered": courses_registered,
    "grades": grades
}
#creating a loist to accomodate more students
students = []
students.append(student_record)

#store data in a text file
with open("student_records.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")



#Data Processing

# 1. Function to add a new course
def add_course(student, course_code):
    if course_code not in student["courses_registered"]:
        student["courses_registered"].append(course_code)
        student["grades"][course_code] = None   # Initialize grade
        print(f"Course {course_code} added successfully.")
    else:
        print(f"Course {course_code} is already registered.")


# 2. Function to update grade
def update_grade(student, course_code, grade):
    if course_code in student["grades"]:
        student["grades"][course_code] = grade
        print(f"grade for {course_code} updated to {grade}.")
    else:
        print(f"{course_code} is not registered for this student.")
#3, Function to calculate gpa
grade_points = {
    'A': 5.0, #I chose 5.0 instead of 5 to implicitly indicate thhat gpa is a float
    'B': 4.0,
    'C': 3.0,
    'D': 2.0,
    'E': 1.0,
    'F': 0.0
}

def calculate_gpa(grades_dict):
    total = 0
    for course, grade in grades_dict.items():
        total += grade_points[grade]
    gpa = total / len(grades_dict)
    return gpa

student_gpa = calculate_gpa(grades)
print("Calculated GPA:", student_gpa)

def generate_report():
    print("===== STUDENT REPORT =====")
    print("name:", student_name)
    print("matric number:", matric_number)
    print("age:", age)
    print("cgpa:", cgpa)
    print("Active:", is_active)
    print("Courses:", courses_registered)
    print("Grades:", grades)
    print("GPA:", calculate_gpa(grades))
   # print("Total Courses:", course_count())
    #print("On Probation?:", is_on_probation(compute_gpa(grades)))
    print("==========================")

generate_report()


# Task 1.2

#store data for atleast 5 studentsz;

#using list of student name
student_names = ["Akinlade Sofiu Gbolahan", "Dada Quadri", "Oyedele Quadri", "Abdulrasaq Boluwatife", "Balogun Ruth"]

#a dictionary for each student
students = [
    {
          "name": "Akinlade Sofiu Gbolahan",
        "matric_no": "22/66MB065",
        "age": 22,
        "cgpa": 4.82,
        "is_active": True,
        "outstanding_courses": 0,
        "courses_registered": courses_registered,
        "departmentInfo": ("Finance Department", "Faculty of Management Sciences", 2025)
    },
    {
        "name": "Dada Quadri",
        "matric_no": "22/66MB177",
        "age": 21,
        "cgpa": 4.11,
        "is_active": True,
        "outstanding_courses": 0,
        "courses_registered": courses_registered,
        "departmentInfo": ("Finance Department", "Faculty of Management Sciences", 2025)
    },
    {
       "name": "Oyedele Quadrin",
        "matric_no": "22/66MB054",
        "age": 20,
        "cgpa": 4.44,
        "is_active": True,
        "outstanding_courses": 0,
        "courses_registered": courses_registered,
        "departmentInfo": ("Finance Department", "Faculty of Management Sciences", 2025)
    },
    {
        "name": "Abdulrasaq Boluwatife",
        "matric_no": "22/66MB012",
        "age": 22,
        "cgpa": 4.15,
        "is_active": True,
        "outstanding_courses": 2,
        "courses_registered": courses_registered,
        "departmentInfo": ("Finance Department", "Faculty of Management Sciences", 2025)
    },
    {
        "name": "Balogun Ruth",
        "matric_no": "22/66MB026",
        "age": 20,
        "cgpa": 3.33,
        "is_active": False,  # Example of inactive student
        "outstanding_courses": 2,
        "courses_registered": courses_registered,
        "departmentInfo": ("Finance Department", "Faculty of Management Sciences", 2025)
    }
]

# 3. Set to store unique courses offered in the department
unique_courses = set()

# Extract all courses from each student's registered courses
for student in students:
    for course in student["courses_registered"]:
        unique_courses.add(course)

# Print results
print("List of student names:", student_names)
print("Unique courses offered in the department:", unique_courses)

#Tuple on fixed department information


#part 2
#Task 2.1 function that accepts scores from 0-100

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"

    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'D'
    elif score >= 40:
        return 'E'
    else:
        return 'F'

    #Using match-case
def grade_feedback(grade):
    match grade:
        case "A":
            print("Excellent performance. Keep it up!")
        case "B":
            print("Very good work. You can do even better.")
        case "C":
            print("Good effort. Try to improve.")
        case "D":
            print("Fair performance. More effort is needed.")
        case "E":
            print("Pass, but improvement is required.")
        case "F":
            print("Fail. You need to work much harder.")
        case _:
            print("Invalid grade.")

score = int(input("Enter student score (0–100): "))

grade = calculate_grade(score)
print("Grade:", grade)

grade_feedback(grade)

# Task 2.2
#Type conversion and validation

def age_and_cgpa():
    try:
        # input as strings
        age = input("Enter student age: ")
        cgpa = input("Enter student cgpa: ")

        # Convert to correct data types
        age = int(age)
        cgpa = float(cgpa)

        # Validation
        if age < 18 or age > 30:
            print("Invalid age. Age must be between 18 and 30.")
            return

        if cgpa < 0.0 or cgpa > 5.0:
            print("Invalid CGPA. CGPA must be between 0.0 and 5.0.")
            return

        print("Valid Age and CGPA")
        print("Age:", age)
        print("CGPA:", cgpa)

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
age_and_cgpa()


# Task 3.1: List Operations and Slicing

# Given list of 10 assignment scores
assignment_scores = [65, 78, 82, 90, 74, 88, 91, 69, 85, 77]

# Extracting the top 3 scores using slicing

arranged_scores = sorted(assignment_scores, reverse=True)
top_3_scores = arranged_scores[:3]
print("Top 3 scores:", top_3_scores)

# Extract the last 5 scores using negative indexing
last_5_scores = assignment_scores[-5:]
print("Last 5 scores:", last_5_scores)


# Extract every other score using step slicing

every_other_score = assignment_scores[::2]
print("Every other score:", every_other_score)



# Task 3.2: Set Operations

# Set of students who passed GSE301
set_pass = {"Akinlade Sofiu Gbolahan", "Dada Quadri", "Oyedele Quadri", "Abdulrasaq Boluwatife"}

# Set of students with CGPA above 4.0 (Merit)
set_merit = {"Akinlade Sofiu Gbolahan",  "Dada Quadri", "Oyedele Quadri", "Abdulrasaq Boluwatife"}


# Students who passed GSE301 AND have merit (Intersection)
passed_and_merit = set_pass.intersection(set_merit)
print("Passed Python and have merit: ", passed_and_merit)


# All distinct students in both sets  (Union)

all_distinct_students = set_pass.union(set_merit)
print("All distinct students:", all_distinct_students)


# Students who passed GSE301 but do NOT have merit(Difference)

passed_but_no_merit = set_pass.difference(set_merit)
print("Passed Python but no merit:", passed_but_no_merit)


# -----------------------------------------
# Task 4.1: Interactive Console Menu System
# -----------------------------------------

students = [
    {"name": "Akinlade Sofiu Gbolahan", "cgpa": 4.82},
    {"name": "Dada Quadri", "cgpa": 4.11},
    {"name": "Oyedele Quadri", "cgpa": 4.44},
    {"name": "Abdulrasaq Boluwatife", "cgpa": 4.15},
    {"name": "Balogun Ruth", "cgpa": 3.33}
]

while True:
    print("===== STUDENT MANAGEMENT MENU =====")
    print("1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    match choice:
        case "1":
            print("\n--- All Students ---")
            for student in students:
                print(student["name"], "- CGPA:", student["cgpa"])
            input("\nPress Enter to return to the menu...")

        case "2":
            name = input("Enter student name: ")
            cgpa = float(input("Enter student CGPA: "))
            students.append({"name": name, "cgpa": cgpa})
            print("Student added successfully.")
            input("Press Enter to continue...")

        case "3":
            name = input("Enter student name: ")
            found = False
            for student in students:
                if student["name"] == name:
                    found = True
                    if student["cgpa"] >= 2.0:
                        print(name, "is eligible for graduation.")
                    else:
                        print(name, "is NOT eligible for gradation.")
            if not found:
                print("Student not found.")
            input("Press Enter to continue...")

        case "4":
            top_student = max(students, key=lambda s: s["cgpa"])
            print("\nTop Performer:")
            print(top_student["name"], "- CGPA:", top_student["cgpa"])
            input("Press Enter to continue...")

        case "5":
            print("Exiting system...")
            break

        case _:
            print("Invalid option. Please select 1–5.")
            input("Press Enter to continue...")



# Task 4.2: Graduation Eligibility Checker


def check_graduation_eligibility(student):
    """
    Checks if a student can graduate where the elegibility criteria are, 2.5 CGPA, no failed courses, and active status.
    """

    # Check each condition
    cgpa_ok = student["CGPA"] >= 2.5
    courses_ok = all(grade not in [None, "F"] for grade in student["Grades"].values())
    is_active = student["is_active"]

    # Combine conditions
    eligible = cgpa_ok and courses_ok and is_active

    # Create message
    if eligible:
        message = f"{student['student_name']} is eligible to graduate \U0001f393"
    else:
        message = f"{student['student_name']} is NOT eligible to graduate.\n"
        reasons = []
        if not cgpa_ok:
            reasons.append(f"CGPA ({student['CGPA']}) is below 2.5")
        if not courses_ok:
            reasons.append("Has failed or incomplete courses")
        if not is_active:
            reasons.append("Student is not active")
        message += "Reasons: " + "; ".join(reasons)

    return eligible, message

#using a dummy student record to test the function
student = {
    "Student_name": "Jimoh Kabir",
    "CGPA": 3.75,
    "is_active": True,
    "Grades": {"FIN311": "C", "FIN317": "A", "GSE301": "B", "FIN323": "A"}
}

eligible, msg = check_graduation_eligibility(student)
print(msg)


# -----------------------------------------
# Task 5.1: Nested Data Processing
# -----------------------------------------

# Sample nested dictionary of students and their course scores
student_scores = {
    "Akinlade Sofiu Gbolahan": {"FIN311": 84, "FIN317": 81, "GSE301": 95, "FIN323": 84},
    "Dada Quadri": {"FIN311": 97, "FIN317": 92, "GSE301": 98, "FIN323": 85},
    "Oyedele Quadri": {"FIN311": 85, "FIN317": 91, "GSE301": 97, "FIN323": 74},
    "Abdulrasaq Boluwatife": {"FIN311": 67, "FIN317": 91, "GSE301": 97, "FIN323": 65},
    "Balogun Ruth": {"FIN311": 56, "FIN311": 67, "GSE301": 92, "FIN323": 90}
}

# Dictionary to store average scores
average_scores = {}

# List to store students who scored above 70 in all courses
top_students = []

# Process each student
for student, courses in student_scores.items():
    scores = courses.values()
    avg_score = sum(scores) / len(scores)
    average_scores[student] = avg_score

    # Check if student scored above 70 in all courses
    if all(score > 70 for score in scores):
        top_students.append(student)
a
# Print average scores
print("Average scores per student:")
for student, avg in average_scores.items():
    print(f"{student}: {avg:.2f}")

# Print students who scored above 70 in all courses
print("\n====Students who scored above 70 in all courses:===")
for student in top_students:
    print(student)



# Task 5.2: Pattern Matching with MATCH CASE


def identify_type(value):
    """
    Identifies the type of the input using match-case
    and returns a formatted summary.
    """
    match value:
        case int():
            return f"Value: {value} is an integer."
        case float():
            return f"Value: {value} is a float."
        case list():
            return f"Value: {value} is a list with {len(value)} elements."
        case dict():
            return f"Value: {value} is a dictionary with {len(value)} key-value pairs."
        case str():
            return f"Value: '{value}' is a string with {len(value)} characters."
        case _:
            return f"Value: {value} is of type {type(value).__name__} (unhandled)."


#Testing the function with different inputs
print(identify_type(42))
print(identify_type(3.14))
print(identify_type([1, 2, 3]))
print(identify_type({"name": "Jones", "age": 20}))
print(identify_type("Hello World"))
print(identify_type(True))  # unhandled type example
