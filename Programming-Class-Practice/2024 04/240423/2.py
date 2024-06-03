#　1 이상 30 이하의 정수 중에 , 짝수이면서 5의 배수를 출력하세요

for count in range(1, 31):
    if count % 2 == 0 and count % 5 == 0:
        print(count,"\t",end="")
