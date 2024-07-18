score_alp_li = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_num_li = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_score = 0
total_credits = 0

for _ in range(20):
    sub, credits, grade = input().split()
    credits = float(credits)
    
    if grade != "P":
        score = score_num_li[score_alp_li.index(grade)]
        total_score += credits * score
        total_credits += credits

if total_credits == 0:
    print("0.000000")
else:
    gpa = total_score / total_credits
    print(f"{gpa:.6f}")
