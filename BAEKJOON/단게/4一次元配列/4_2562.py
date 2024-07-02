numbers = []

for i in range(1,10):
    number = int(input())
    numbers.append(number)
    
maxN = max(numbers)

print(maxN)
print(numbers.index(maxN)+1)