#grades

student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60,
}

student_grades = {}

for estudiante in student_scores:
    nota= student_scores[estudiante]

    if nota >90:
        grade= "Outstanding"
    elif nota >80:
        grade= "Exceeds Expectations"
    elif nota >70:
        grade= "Acceptable"
    else:
        grade= "Fail"

    student_grades[estudiante]= grade

print(student_grades)
   