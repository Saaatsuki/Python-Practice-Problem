import random

print("난수를 생성할 범위와 개수를 입력하세요.")

start = int(input("Start (0 이상의 장수) : "))
while not 0 <= start:
    print("0이상의 정수를 입력하세요.")
    start = int(input("Start (0 이상의 장수) : "))
end = int(input("End (Start 보다 큰 장수) : "))
while not start <= end:
    print(f"End는 Start({start})보다 커야 합니다.")
    end = int(input("End (Start 보다 큰 장수) : "))
N = int(input("N (생성할 난수의 개수) : "))
while not 1 <= N <= 2:
    print("N은 1부터 2사이의 정수여야 힙나다.")
    N = int(input("N (생성할 난수의 개수) : "))

li = []
count = 0
while count < N:
    count += 1
    num = random.randint(start , end)
    if not num in li:
        li.append(num)

print(f"생성된 난수 리스트 : \n{li}")
