grade_categories = (
    ("Excellent", 80, 100),
    ("Good", 60, 80),
    ("Pass", 40, 60),
    ("Fail", 0, 40)
)

def classify_grade(score):
    for grade, minimum, maximum in grade_categories:
        if minimum <= score < maximum:
            return grade
    
    if score == 100:
        return "Excellent"

    return "Invalid"


def collect_student_data():
    students = []
    while True:
        try:
            number = int(input("How many students? (minimum 5): "))

            if number >= 5:
                break

            print("Please enter at least 5 students.")

        except ValueError:
            print("Error: Please enter a whole number.")
    
    for i in range(number):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        study_hours = input("Enter Study Hours: ")
        while True:
            try:
                python_score = float(input("Enter Python Score (0-100): "))

                if 0 <= python_score <= 100:
                    break

                print("Invalid score! Enter a score between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")
        student = {
            "name": name,
            "age": age,
            "study_hours": study_hours,
            "python_score": python_score
        }

        
        students.append(student)
    return students

def calculate_average(students):
    total = 0

    for student in students:
        total += student["python_score"]

    return total / len(students)

def count_passing_students(students):
    count = 0

    for student in students:
        if student["python_score"] >= 40:
            count += 1

    return count

def display_performance_report(students):
    """Display a complete student performance report."""
    print("\n" + "=" * 85)
    print("             STUDENT PERFORMANCE REPORT")
    print("=" * 85)

    for student in students:
        score = student["python_score"]
        grade = classify_grade(score)

        if score >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print(
            f"Name: {student['name']}\n"
            f"Age: {student['age']}\n"
            f"Study Hours{student['study_hours']}\n"
            f"Score: {score}\n"
            f"Grade: {grade}\n"
            
        )

    total_students = len(students)
    average_score = calculate_average(students)
    highest_score = max(s["python_score"] for s in students)
    lowest_score = min(s["python_score"] for s in students)
    passed_students = count_passing_students(students)
    failed_students = total_students - passed_students
    # Find the top student
    top_student = max(
                students,
                key=lambda s: s["python_score"]
            )
    
    # Display summary
    print("===== SUMMARY =====")
    print(f"Total Students: {total_students}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Highest Score: {highest_score:g}")
    print(f"Lowest Score: {lowest_score:g}")
    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")
    print(
        f"Top Student: {top_student['name']} "
        f"({top_student['python_score']:g})"
    )
        
students= collect_student_data()
display_performance_report(students)
        
        



