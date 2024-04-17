def count_number (number):
    if number == 11 or number == 12 or number == 13:
        return str(number) + "th"
    elif number % 10 == 1:
        return str(number) + "st"
    elif number % 10 == 2:
        return str(number) + "nd"
    elif number % 10 == 3:
        return str(number) + "rd"
    else:
        return str(number) + "th"    
    

print(count_number(int(input("Please enter an integer (1-99) : "))))