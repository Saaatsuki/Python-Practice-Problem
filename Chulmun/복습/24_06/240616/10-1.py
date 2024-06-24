book_li = []
while "중료" not in book_li:
    book = input("도서 제목을 입력하세요 (중료) : ")
    book_li.append(book)

book_li.remove("중료")
print(f"도서 제목 : {book_li}")
