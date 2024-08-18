T = int(input())
for i in range(1, T+1):
    scores = list(map(int, input().split()))[1:]  # 첫 번째 숫자는 학생 수이므로 제외
    scores.sort(reverse=True)
    max_score = scores[0]
    min_score = scores[-1]
    largest_gap = max(scores[j] - scores[j+1] for j in range(len(scores) - 1))
    print(f"Class {i}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
