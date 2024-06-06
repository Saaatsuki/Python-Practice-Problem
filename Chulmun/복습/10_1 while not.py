book_list = []
book = ""
while not book == "종료":
    book = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력) : ")
    if book != "종료":
        book_list.append(book)
book_list_join = "  ❤  ".join(book_list)
print(f"도서 목록 : {book_list_join}")