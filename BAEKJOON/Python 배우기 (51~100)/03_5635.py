game_count = int(input())

name_li = []
year_li = []
mon_li = []
day_li = []

for _ in range(game_count):
    name,str_day,str_mon,str_year = input().split()
    day = int(str_day)
    mon = int(str_mon)
    year = int(str_year) 

    year_li.append(year)
    mon_li.append(mon)
    day_li.append(day)
    name_li.append(name)

max_index = 0
for i in range(1, game_count):
    if (year_li[i] > year_li[max_index] or
        (year_li[i] == year_li[max_index] and mon_li[i] > mon_li[max_index]) or
        (year_li[i] == year_li[max_index] and mon_li[i] == mon_li[max_index] and day_li[i] > day_li[max_index])):
        max_index = i

min_index = 0
for i in range(1, game_count):
    if (year_li[i] < year_li[min_index] or
        (year_li[i] == year_li[min_index] and mon_li[i] < mon_li[min_index]) or
        (year_li[i] == year_li[min_index] and mon_li[i] == mon_li[min_index] and day_li[i] < day_li[min_index])):
        min_index = i
        
print(name_li[max_index])
print(name_li[min_index])