numberT = int(input("受け取る値の数を入力してください："))

for _ in range(numberT):
    numA,numB = map(int,input("AとBの値を入力してください：").split())
    print(numA + numB)
