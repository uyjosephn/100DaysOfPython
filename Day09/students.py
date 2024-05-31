students_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in students_score:
    if students_score[student] > 90:
        student_grades[student] = "Outstanding"
    elif students_score[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif students_score[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)