import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Module 1: Student Registration
# -------------------------------

def student_registration():
    print("\n=== Student Registration ===")

    name = input("Enter student name: ")
    score = float(input("Enter exam score: "))

    if 90 <= score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("Remark:", remark)


# -----------------------------------
# Module 2: Course Enrollment System
# -----------------------------------

def course_enrollment():
    print("\n=== Course Enrollment ===")

    courses = []
    max_courses = 5

    while True:

        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done'): ")

        if course_name.lower() == "done":
            break

        credits = input("Enter course credits: ")

        if not credits.isdigit():
            print("Invalid credits! Skipping...")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credits must be positive!")
            continue

        courses.append((course_name, credits))
        print("Course added successfully.\n")

    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")

    print("Total Courses:", len(courses))


# -----------------------------------------
# Module 3: Student Record Management
# -----------------------------------------

def student_records():
    print("\n=== Student Records ===")

    students = [
        {"name": "Priya", "age": 20, "grades": [85, 90, 78]},
        {"name": "Rahul", "age": 21, "grades": [72, 88, 91]},
        {"name": "Anita", "age": 19, "grades": [95, 89, 92]}
    ]

    for student in students:
        print("\nName:", student["name"])
        print("Age:", student["age"])
        print("Grades:", student["grades"])

    event_A = {"Priya", "Rahul", "Anita"}
    event_B = {"Rahul", "Anita", "Sneha"}

    print("\nCommon Participants:", event_A & event_B)
    print("All Participants:", event_A | event_B)
    print("Only Event A:", event_A - event_B)


# -------------------------------------
# Module 4: Sorting and Searching
# -------------------------------------

def sorting_searching():
    print("\n=== Sorting and Searching ===")

    student_ids = [105, 102, 110, 108, 101, 115]

    print("Original IDs:", student_ids)

    # Bubble Sort
    n = len(student_ids)

    for i in range(n):
        for j in range(0, n - i - 1):

            if student_ids[j] > student_ids[j + 1]:
                student_ids[j], student_ids[j + 1] = student_ids[j + 1], student_ids[j]

    print("Sorted IDs:", student_ids)

    # Linear Search
    target = int(input("Enter ID to search: "))

    found = False

    for i in range(len(student_ids)):
        if student_ids[i] == target:
            print("ID found at index", i)
            found = True
            break

    if not found:
        print("ID not found")


# -----------------------------------
# Module 5: Fee Calculation
# -----------------------------------

def calculate_fee(tuition, hostel=0, transport=0):
    return tuition + hostel + transport


def fee_management():
    print("\n=== Fee Calculation ===")

    tuition = float(input("Enter tuition fee: "))
    hostel = float(input("Enter hostel fee: "))
    transport = float(input("Enter transport fee: "))

    total = calculate_fee(tuition, hostel, transport)

    print("Total Fee:", total)


# -----------------------------------
# Module 6: File Handling
# -----------------------------------

def file_handling():
    print("\n=== File Handling ===")

    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")

    print("Records written successfully.")

    print("\nReading Records:")

    with open("student_records.txt", "r") as file:
        records = file.readlines()

        for record in records:
            print(record.strip())


# -----------------------------------
# Module 7: Directory Scanner
# -----------------------------------

class MissingFileOrFolderError(Exception):
    pass


def scan_directory(path):

    try:
        if not os.path.exists(path):
            raise FileNotFoundError("Invalid directory path!")

        for root, dirs, files in os.walk(path):

            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level

            print(f"{indent}{os.path.basename(root)}/")

            sub_indent = " " * 4 * (level + 1)

            for f in files:
                print(f"{sub_indent}{f}")

            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

    except FileNotFoundError as e:
        print("Error:", e)

    except MissingFileOrFolderError as e:
        print("Custom Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)


def directory_management():
    print("\n=== Directory Scanner ===")

    path = input("Enter directory path: ")

    scan_directory(path)


# -----------------------------------
# Module 8: Performance Analytics
# -----------------------------------

def performance_analysis():

    print("\n=== Performance Analysis ===")

    try:
        df = pd.read_csv("student_performance.csv")

        print("\n--- Raw Data ---")
        print(df)

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy()

        mean_scores = np.mean(scores, axis=0)

        print("\nAverage Scores:", mean_scores)

        subjects = ["Math", "Science", "English"]

        plt.bar(subjects, mean_scores)

        plt.title("Average Scores per Subject")

        plt.xlabel("Subjects")
        plt.ylabel("Scores")

        plt.show()

    except FileNotFoundError:
        print("CSV file not found!")

    except Exception as e:
        print("Unexpected Error:", e)


# -----------------------------------
# Main Menu System
# -----------------------------------

while True:

    print("\n========== SMART CAMPUS INFORMATION SYSTEM ==========")

    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Student Records")
    print("4. Sorting and Searching")
    print("5. Fee Calculation")
    print("6. File Handling")
    print("7. Directory Scanner")
    print("8. Performance Analytics")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student_registration()

    elif choice == "2":
        course_enrollment()

    elif choice == "3":
        student_records()

    elif choice == "4":
        sorting_searching()

    elif choice == "5":
        fee_management()

    elif choice == "6":
        file_handling()

    elif choice == "7":
        directory_management()

    elif choice == "8":
        performance_analysis()

    elif choice == "9":
        print("Exiting Smart Campus Information System...")
        break

    else:
        print("Invalid choice! Please try again.")