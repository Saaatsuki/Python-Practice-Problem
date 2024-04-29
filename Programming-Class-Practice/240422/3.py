# number = int(input("星の数を入力してください\n"))
# star_number = number

# while (star_number > 0):
#     print("　"*(star_number-number)+"★"*star_number)
#     star_number -=1
    
number = int(input("整数を入力してください: "))
star_number = number


while star_number > 0:
    print(" " * (number - star_number) + "★" * star_number)
    star_number -= 1