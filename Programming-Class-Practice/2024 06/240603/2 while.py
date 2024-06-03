#17)음수 또는 0인 경우 재입력 -> 양수가 입력 될 때 까지
#   負の数 または０の場合再入力　→　正の数が入力されるまで

input17 = int(input("整数を入力してください："))

while not input17>0:
    input17 = int(input("1以上の整数を入力してください："))\
        

#18)
list18 = ["Hello","World","Cheol"]    
found_word = False  
for i in list18:
    if i == "world":
        print("単語を見つけました")
        found_word = True
    print(i)
    
if not found_word :
    print("単語を見つけることができませんでした。ぴえん")