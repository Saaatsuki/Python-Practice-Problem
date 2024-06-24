scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

score_main = [90, 80, 70, 60, 0]
alp_list = ["A", "B", "C", "D", "F"]

print("등급 분포 및 평균 점수:")
for i in range(len(score_main)):
    filtered_scores = [scores.pop(scores.index(score)) for score in scores if score >= score_main[i]]
    num_students = len(filtered_scores)
    average_score = sum(filtered_scores) / num_students if num_students > 0 else 0

    print(f"{alp_list[i]} 등급 : 평균 점수 = {average_score:.2f}\n{'*' * num_students} ({num_students}명)")