import csv  # Import CSV

# Load data from file
def load_student_data(filename):
    with open(filename, 'r') as file:  # Open file
        reader = csv.reader(file)  # Read CSV
        num_students = int(next(reader)[0])  # Number of students
        students = []  # Student list
        for row in reader:  # Loop rows
            students.append({
                'id': int(row[0]),
                'name': row[1],
                'coursework_marks': list(map(int, row[2:5])),  # Coursework
                'exam_mark': int(row[5])  # Exam mark
            })
    return num_students, students  # Return data

# Calculate student stats
def calculate_student_data(student):
    total_coursework = sum(student['coursework_marks'])  # Total coursework
    total_score = total_coursework + student['exam_mark']  # Total score
    percentage = (total_score / 160) * 100  # Percentage
    grade = 'A' if percentage >= 70 else 'B' if percentage >= 60 else 'C' if percentage >= 50 \
        else 'D' if percentage >= 40 else 'F'  # Grade
    return total_coursework, student['exam_mark'], percentage, grade  # Return stats

# View all student records
def view_all_students(students):
    total_percentage = 0  # Initialize total percentage
    for student in students:
        total_coursework, exam_mark, percentage, grade = calculate_student_data(student)
        print(f"Name: {student['name']}, ID: {student['id']}, Coursework: {total_coursework}, "
              f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")
        total_percentage += percentage
    avg_percentage = total_percentage / len(students)  # Calculate average
    print(f"\nClass Summary: Total Students: {len(students)}, Average Percentage: {avg_percentage:.2f}%")

# View individual student record
def view_individual_student(students):
    student_id = int(input("Enter student ID: "))
    student = next((s for s in students if s['id'] == student_id), None)  # Find student
    if student:
        total_coursework, exam_mark, percentage, grade = calculate_student_data(student)
        print(f"Name: {student['name']}, ID: {student['id']}, Coursework: {total_coursework}, "
              f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")
    else:
        print("Student not found.")

# Show student with highest score
def show_highest_score(students):
    highest_student = max(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])  # Max score
    total_coursework, exam_mark, percentage, grade = calculate_student_data(highest_student)
    print(f"\nTop Student: {highest_student['name']}, ID: {highest_student['id']}, Coursework: {total_coursework}, "
          f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")

# Show student with lowest score
def show_lowest_score(students):
    lowest_student = min(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])  # Min score
    total_coursework, exam_mark, percentage, grade = calculate_student_data(lowest_student)
    print(f"\nLowest Scoring Student: {lowest_student['name']}, ID: {lowest_student['id']}, Coursework: {total_coursework}, "
          f"Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")

# Main menu
def main_menu():
    num_students, students = load_student_data("C:\\Users\\kashi\\.spyder-py3\\studentMarks.txt")
    while True:
        print("\nMenu:\n1. View all student records\n2. View individual student record\n"
              "3. Show student with highest score\n4. Show student with lowest score\n5. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            view_all_students(students)
        elif choice == '2':
            view_individual_student(students)
        elif choice == '3':
            show_highest_score(students)
        elif choice == '4':
            show_lowest_score(students)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main_menu()
