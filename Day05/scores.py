student_scores = input().split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
print(max(student_scores))