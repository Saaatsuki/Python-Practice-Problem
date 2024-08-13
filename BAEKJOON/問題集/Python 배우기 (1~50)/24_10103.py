T = int(input())

score_a = 100
score_b = 100
for _ in range(T):
    num1 , num2 = map(int,input().split())
    
    if num1 < num2:
        score_a -= num2
    elif num1 > num2:
        score_b -= num1
    
print(f"{score_a}\n{score_b}")
    