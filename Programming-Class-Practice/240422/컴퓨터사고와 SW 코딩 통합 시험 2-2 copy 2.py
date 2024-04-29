number = int(input("整数を入力してネ★："))
star_number = number

while (star_number>0):
    print(" "*(number - star_number)+"★"*star_number)
    star_number -= 1