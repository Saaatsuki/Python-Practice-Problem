score_li = []
for _ in range(5):
    input_score = int(input())
    if input_score<=40:
        score = 40
    else:
        score = input_score
    score_li.append(score)

score_li_max = sum(score_li)
score_li_avg = score_li_max / 5
print(int(score_li_avg))