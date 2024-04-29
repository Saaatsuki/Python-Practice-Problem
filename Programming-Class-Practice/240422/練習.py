#양의 정수 5개를 입력 받아, 합과 평균을 출력하는 프로그램을 작성하시오.
#正の整数 5 つを入力してもらい、和と平均を出力するプログラムを作成しなさい。
input_value_1 = int(input("1번째 값 : "))
input_value_2 = int(input("2번째 값 : "))
input_value_3 = int(input("3번째 값 : "))
input_value_4 = int(input("4번째 값 : "))
input_value_5 = int(input("5번째 값 : "))

sum = input_value_1 + input_value_2 + input_value_3 + input_value_4 + input_value_5
avg = sum / 5

print("sum: ", sum, "\tavg: ", avg)