subject = int(input())

scores = list(map(int,input().split()))

m = max(scores)


for i in range(subject):
    scores[i] = scores[i]/m*100
    
    
print(sum(scores)/subject)