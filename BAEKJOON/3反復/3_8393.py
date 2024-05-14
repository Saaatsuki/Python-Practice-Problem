number = int(input())
numbers = []

for i in range(1,number+1):
    numbers.append(i)
    
answer = 0
for n in numbers:
    answer += n
print(answer)