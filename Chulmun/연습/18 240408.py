books = []

while True:
    title = input("Please enter a title for the book : ")
    if title == "Finish":
        break
    books.append(title)
    
print("The titles of all the books on the list(To finish, enter 'Finish')",f'{books}')
