check_year = int(input("Please enter the Western calendar you want to check if it is a leap year╰(*°▽°*)╯ : "))

msg = "That year is a {} （￣︶￣）↗!!!!!!"

if (check_year % 4 == 0 and check_year % 100 != 0) or (check_year % 400 == 0):
    print(msg.format("leap year"))
else:
    print(msg.format("not leap year"))