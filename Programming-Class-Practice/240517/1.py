msg = "hello"

for char in msg:
# hello -> 1st : h , 2nd : e , 3rd : l , 4th : l
    print(msg)
    # msg = "hello"


for char in (msg := "hello"):
    print(msg)