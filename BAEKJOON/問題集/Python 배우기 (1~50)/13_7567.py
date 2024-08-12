# boul = list(input())

# answer = 10

# boul.remove(boul[0])

# for i in boul:
#     if i == "(":
#         answer += 5
#     elif i == ")":
#         answer += 10

# print(answer)

boul = list(input())

answer = 10

for i in range(1,len(boul)):
    if boul[i] == boul[i-1]:
        answer += 5  
    else:
        answer += 10  # 

print(answer)
