score = [99,29,30,40,20,60]

# 학생 수
student_count = len(score)

# 학생 총합
# score_count = sum(score)
score_count = 0
for i in score:
    score_count += i

# 학생 평균
average = score_count / student_count

print(f"학생 수 : {student_count} , 충정 : {score_count} , 평균 : {average}")