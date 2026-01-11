# student.py
# Program to calculate student grade

import sys

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def assign_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def main():
    print("=== Student Grade Calculator ===")

    try:
        # Command-line input
        if len(sys.argv) == 7:
            name = sys.argv[1]
            department = sys.argv[2]
            semester = int(sys.argv[3])
            m1 = float(sys.argv[4])
            m2 = float(sys.argv[5])
            m3 = float(sys.argv[6])

        # User input
        else:
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            semester = int(input("Enter Semester: "))
            m1 = float(input("Enter marks in Subject 1: "))
            m2 = float(input("Enter marks in Subject 2: "))
            m3 = float(input("Enter marks in Subject 3: "))

        print("\n--- Student Details ---")
        print("Student Name :", name)
        print("Department   :", department)
        print("Semester     :", semester)
        print("Marks        :", m1, m2, m3)

        average = calculate_average(m1, m2, m3)
        grade = assign_grade(average)

        print("\nAverage :", f"{average:.2f}")
        print("Grade   :", grade)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()