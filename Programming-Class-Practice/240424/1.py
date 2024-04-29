number = int(input("整数を入力してください: "))
star_number = number

while star_number > 0:
    print(" " * (number - star_number) + "*" * star_number)
    star_number -= 1