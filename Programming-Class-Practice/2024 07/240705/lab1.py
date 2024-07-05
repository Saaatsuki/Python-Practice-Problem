print("난수를 생성할 범위와 개수를 입력하세요")

start = int(input("Start (0 이상의 정수) : "))
while not 0 <= start:
    start = int(input("Start (0 이상의 정수) : "))
end = int(input("End (Start 보다 큰 정수 ) : "))
while not start < end:
    end = int(input(f"End는 Start({start})보다 커야 합니다.\nEnd (Start 보다 큰 정수 ) : "))

num = int(input("N (생성할 난수의 개수) : "))
while not 1<= num <= 2:
    num = int(input("N은 1부터 2사이의 정수여야 합니다.\nN (생성할 난수의 개수) : "))

