import pandas as pd

# The data does not have the overall weight of each type, so we store that here
lab_weight = .9
attendance_weight = .1

# load the data and print it.  Note, this program expects to be run from the lab 1 folder
grades = pd.read_csv("data/grades.csv")
print(grades)

# calculate the points earned for each assignment
grades["Points"] = grades.Grade / grades.MaxGrade * 100 * grades.TypeWeight

print("\nPoints for each assignment")
print(grades)

# Now do a weighted average for each type, and add the overall weight for each type
type_grades = grades.groupby("Type")[["Points"]].sum()
type_grades["Weight"] = lab_weight
type_grades.loc["attendance", "Weight"] = attendance_weight
print("\nGrades on Labs and Attendance")
print(type_grades)

# lastly, do a weighted sum to find the final grade
final_grade = (type_grades.Points * type_grades.Weight).sum()

print(f"\nFinal Grade = {final_grade}")
