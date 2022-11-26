# Program for student grades by using the dictionaries

student_Scores = {
    "john": 93,
    "peter": 85,
    "lucifer": 75,
    "jenny": 87,
    "jessie": 100
}
student_Grades = {}

for student in student_Scores:
    score = student_Scores[student]
    if score > 90:
        student_Grades[student] = "Outstanding"
    elif score > 80:
        student_Grades[student] = "Great"
    elif score > 70:
        student_Grades[student] = "Acceptable"
    else:
        student_Grades[student] = "Fail"

print(student_Grades)