numbers = [int(input(f"{i}번째 수 입력 : ")) for i in ["첫", "두", "세"]]

max_number = numbers[0]
for i in numbers:
    if i >= numbers[0]:
        max_number = i

numbers_set = set(numbers)
remove_num = [i for i in numbers if numbers.count(i)>1]

if numbers[0] != numbers[1] != numbers[2]:
    print(f"모든 수가 다릅니다.가장 큰 수는 {max_number}입니다.")
elif len(numbers_set)==2:
    print(f"두 수가 같습니다.{remove_num[0]}")
else:
    print(f"모든 수가 같습니다.{numbers[0]}")