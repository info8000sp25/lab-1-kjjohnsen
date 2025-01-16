import pandas as pd

# Define weights for each grade type
LAB_WEIGHT = 0.9
ATTENDANCE_WEIGHT = 0.1

# Load the data and display it
# Note: This program expects to be run from the "lab 1" folder
grades = pd.read_csv("data/grades.csv")
print("Initial Grades Data:")
print(grades)

# Calculate the points earned for each assignment
grades["Points"] = (grades.Grade / grades.MaxGrade) * 100 * grades.TypeWeight

print("\nPoints for Each Assignment:")
print(grades)

# Calculate weighted sum of points for each type and assign weights
type_grades = grades.groupby("Type")[["Points"]].sum()
type_grades["Weight"] = LAB_WEIGHT
type_grades.loc["attendance", "Weight"] = ATTENDANCE_WEIGHT

print("\nGrades by Type (Labs and Attendance):")
print(type_grades)

# Compute the final grade as a weighted sum
final_grade = (type_grades.Points * type_grades.Weight).sum()

print(f"\nFinal Grade: {final_grade:.2f}")
