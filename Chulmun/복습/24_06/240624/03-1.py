def getIn(argSequence,argValue):
    for val in argSequence:
        if val == argValue:
            return True
    return False
    
code_li = ["E1","E2","E3"]

age = int(input("年齢を入力すむちゃむ💛："))
while age<1:
    age = int(input("正しい年齢を入力すむちゃむ💛："))
code = input("予約コードを入力するちゃむ💛：")
while not getIn(code_li,code):
    code = input(f"{code_li}の中から、予約コードを入力するちゃむ💛：")
date = int(input("予約の日付を入力するちゃむ💛："))
while not 1<=date<=31:
    date = int(input("正しい予約の日付を入力するちゃむ💛："))

booking_TF = False
age_Tf = True
date_TF = True

if code == "E1":
    if 18<=age:
        booking_TF = True
    else:
        age_Tf = False

if code == "E2":
    if date%2==0:
        booking_TF = True
    else:
        date_TF = False

if code == "E3":
    if 16>age and date%7!=0:
        age_Tf = False
        date_TF = False
    elif 16>age:
        age_Tf = False
    elif date%7!=0:
        date_TF = False
    else:
        booking_TF = True

if booking_TF:
    msg = "予約完了したちゃむ💙"
elif not date_TF:
    msg = "日付が原因で予約できないちゃむ💙"
elif not age_Tf:
    msg = "年齢が足らないちゃむ💙"
elif not date_TF and not age_Tf:
    msg = "日付もあかんし、年齢も足りないちゃむよ～💙"

print(msg)