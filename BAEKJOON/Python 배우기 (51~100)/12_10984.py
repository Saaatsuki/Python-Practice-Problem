# test_count = int(input())

# tani_li = []
# hyouka_li = []
# for _ in range(test_count):
#     kamoku_count = int(input())
#     for _ in range(kamoku_count):
#         tani , hyouka = input().split()
#         tani_li.append(int(tani))
#         hyouka_li.append(float(hyouka))
#         print(f"{sum(tani_li)} {(sum(hyouka_li)/len(hyouka_li)):.1f}")

# 入力を読み取る
T = int(input())  # 学期の数

for _ in range(T):
    N = int(input())  # 科目の数
    
    total_credits = 0
    total_grade_points = 0.0
    
    for _ in range(N):
        C, G = map(float, input().split())
        total_credits += int(C)
        total_grade_points += int(C) * G
    
    GPA = total_grade_points / total_credits if total_credits != 0 else 0
    print(f"{total_credits} {GPA:.1f}")
