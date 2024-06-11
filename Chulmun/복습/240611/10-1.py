book = ""
book_li = []
while not book=="종료":
    book = input("도서 제목을 입력하세요 (종료하려면 '총료' 입력) : ")
    book_li.append(book)
del book_li[len(book_li)-1]
print(f"도서 목록 : {book_li}")