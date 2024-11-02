import csv

# Load data
def load_student_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        num_students = int(next(reader)[0])
        students = [{'id': int(row[0]), 'name': row[1], 'coursework_marks': list(map(int, row[2:5])), 'exam_mark': int(row[5])} for row in reader]
    return num_students, students

# Save data
def save_student_data(filename, students):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([len(students)])
        for s in students:
            writer.writerow([s['id'], s['name'], *s['coursework_marks'], s['exam_mark']])

# Calculate
def calculate_student_data(student):
    total = sum(student['coursework_marks']) + student['exam_mark']
    percentage = (total / 160) * 100
    grade = 'A' if percentage >= 70 else 'B' if percentage >= 60 else 'C' if percentage >= 50 else 'D' if percentage >= 40 else 'F'
    return total, student['exam_mark'], percentage, grade

# View all
def view_all_students(students):
    for student in students:
        total_coursework, exam_mark, percentage, grade = calculate_student_data(student)
        print(f"Name: {student['name']}, ID: {student['id']}, Coursework: {total_coursework}, Exam: {exam_mark}, Percentage: {percentage:.2f}%, Grade: {grade}")

# View individual
def view_individual_student(students):
    student = next((s for s in students if s['id'] == int(input("Enter student ID: "))), None)
    if student:
        print(f"Name: {student['name']}, ID: {student['id']}, {calculate_student_data(student)}")
    else:
        print("Not found.")

# Show highest
def show_highest_score(students):
    highest_student = max(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])
    print(f"Top Student: {highest_student['name']}, ID: {highest_student['id']}, {calculate_student_data(highest_student)}")

# Show lowest
def show_lowest_score(students):
    lowest_student = min(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'])
    print(f"Lowest Student: {lowest_student['name']}, ID: {lowest_student['id']}, {calculate_student_data(lowest_student)}")

# Sort
def sort_student_records(students):
    sorted_students = sorted(students, key=lambda s: sum(s['coursework_marks']) + s['exam_mark'], reverse=input("Sort by (1) Ascending or (2) Descending? ") == '2')
    view_all_students(sorted_students)

# Add
def add_student_record(students, filename):
    student = {'id': int(input("ID: ")), 'name': input("Name: "), 'coursework_marks': [int(input(f"Mark {i+1}: ")) for i in range(3)], 'exam_mark': int(input("Exam mark: "))}
    students.append(student)
    save_student_data(filename, students)
    print("Added.")

# Delete
def delete_student_record(students, filename):
    student = next((s for s in students if s['id'] == int(input("ID to delete: "))), None)
    if student:
        students.remove(student)
        save_student_data(filename, students)
        print("Deleted.")
    else:
        print("Not found.")

# Update
def update_student_record(students, filename):
    student = next((s for s in students if s['id'] == int(input("ID to update: "))), None)
    if student:
        choice = input("1. Coursework\n2. Exam\nChoose: ")
        if choice == '1':
            student['coursework_marks'] = [int(input(f"New mark {i+1}: ")) for i in range(3)]
        elif choice == '2':
            student['exam_mark'] = int(input("New exam mark: "))
        save_student_data(filename, students)
        print("Updated.")
    else:
        print("Not found.")

# Main menu
def main_menu():
    filename = "studentMarks.txt"
    num_students, students = load_student_data(filename)
    
    while True:
        choice = input("\n1. View All\n2. View Individual\n3. Top Student\n4. Lowest Student\n5. Sort\n6. Add\n7. Delete\n8. Update\n9. Exit\nChoose: ")
        if choice == '1': view_all_students(students)
        elif choice == '2': view_individual_student(students)
        elif choice == '3': show_highest_score(students)
        elif choice == '4': show_lowest_score(students)
        elif choice == '5': sort_student_records(students)
        elif choice == '6': add_student_record(students, filename)
        elif choice == '7': delete_student_record(students, filename)
        elif choice == '8': update_student_record(students, filename)
        elif choice == '9': break
        else: print("Invalid choice.")

# Run
main_menu()
