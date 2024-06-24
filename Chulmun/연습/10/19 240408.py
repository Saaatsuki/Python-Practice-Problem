menus = ["Pizza","Pasta","Salad","Sushi","Burger"]

index = int(input("Please select an index for the menu(Start from 0) : "))

if (0 <= index <= (len(menus)-1)):
    print("The menu you chose is",menus[index])
else:
    print("Invalid number")