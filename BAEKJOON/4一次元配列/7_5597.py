import sys

classesA = [i for i in range(1, 31)]
# for classA in range(1,31):
#     classesA.append(classA)
    
input = sys.stdin.readlines

numbers = input()

print(numbers)

for number in numbers:
    number = number.strip()
    classesA.remove(int(number))

print(min(classesA))
print(max(classesA))
