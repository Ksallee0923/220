# Kayla S.
# module_02_case_study.py
# This app asks for student names and GPAs. It checks if each student qualifies
# for the Dean's List (GPA 3.5 or higher) or the Honor Roll (GPA 3.25 or higher).
# The program stops when the user enters 'ZZZ' as the last name.

# Test with at least five students

test_data = [
    ("Smith", "Emily", 3.6),
    ("Johnson", "Noah", 3.3),
    ("Brown", "Olivia", 3.1),
    ("Davis", "Liam", 3.5),
    ("Taylor", "Ava", 3.25)
]

for last_name, first_name, gpa in test_data:
    print(f"\nStudent: {first_name} {last_name} - GPA: {gpa}")
    if gpa >= 3.5:
        print("Congratulations! You made the Dean's List.")
    elif gpa >= 3.25:
        print("Great job! You made the Honor Roll.")
    else:
        print("Keep working hard!")

# Allow user input afterward
while True:
    last_name = input("\nEnter student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        break

    first_name = input("Enter student's first name: ")

    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a number.")
        continue

    print(f"\nStudent: {first_name} {last_name} - GPA: {gpa}")
    
    if gpa >= 3.5:
        print("Congratulations! You made the Dean's List.")
    elif gpa >= 3.25:
        print("Great job! You made the Honor Roll.")
    else:
        print("Keep working hard!")