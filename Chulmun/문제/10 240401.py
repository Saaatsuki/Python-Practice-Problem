# ユーザーに自然数を入力してもらう
number = int(input("Please enter a natural number : "))

for star_number_up in range (1,number):
    print("*"*star_number_up)
for star_number_down in range (number,0,-1):
    print("*"*star_number_down)