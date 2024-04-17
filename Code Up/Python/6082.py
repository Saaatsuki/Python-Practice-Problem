# 30以下の整数を受け取る

n = int(input())

# 1からnまでの数に対してループを実行する
for i in range(1 , n+1):
    number = str(i) # 数字を文字列に変換
    
    if '3' in number or '6' in number or '9' in number:
        # 拍手を表す文字列 'X' を count 回繰り返して出力する
        print('X'*count,end='') 
    # 含まれない場合はそのまま数字を出力する
    else:
        print(number,end='')
    
    # 10の倍数であれば改行を行う
    if i % 10 ==0:
        print()
        


n = int(input())

for i in range(1,n+1):
    if (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print("X",end=" ")
    else:
        print(i,end=" ")