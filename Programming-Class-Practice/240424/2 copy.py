star_number = int(input('星の数を入力してネ：'))

for number in range(star_number,0,-1):
    print(' '*(star_number - number) + '★'*number)