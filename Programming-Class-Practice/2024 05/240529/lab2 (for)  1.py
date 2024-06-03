numbers = []
for i in range(1,1000):
    if i % 3 ==0:
        number = i
        numbers.append(number)

count = 0
for i in numbers:
    count += i

print(count)


