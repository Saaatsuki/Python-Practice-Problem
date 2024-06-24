num1 = int(input("기본값을 입력하세요 : "))
select = int(input("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n선댁 : "))
while not 1<=select<=4:
    select = int(input("1~4부터 선택하세요.\n1.더하기\n2.빼기\n3.곱하기\n4.나누기\n선댁 : "))
num2 = int(input("숫자 입력 : "))
while select==4 and num2==0:
    num2 = int(input("에러 : 0으로 나눌 수 없습니다.\n0이외의 숫자 입력 : "))
ans = num1+num2 if select==1 else num1-num2 if select==2 else num1*num2 if select==3 else num1/num2
print(f"연산 결과 : {ans:.1f}")