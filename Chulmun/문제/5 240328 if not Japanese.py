# ユーザーから年齢、予約コード、予約日を入力してもらいます
age = int(input("Please enter your age🐼："))
event_code = input("Please enter your reservation code🐰：")
reservation_date = int(input("Please enter a reservation date🐨："))

# イベント情報を含む辞書を定義します
events = {
    "E1": {"age_limit": 18, "date_restrictions": None},# イベント1: 年齢制限あり、日付制限なし
    "E2": {"age_limit": None, "date_restrictions": "even"},# イベント2: 年齢制限なし、日付が偶数の日のみ
    "E3": {"age_limit": 16, "date_restrictions": "multiple_of_7"}# イベント3: 年齢制限あり(16歳以上)、日付が7の倍数の日のみ
}

# イベントコードが有効かどうかを確認します
if event_code not in events:
    print("Invalid event code. Exiting the program.")# 予約日が1から30の範囲外の場合、エラーメッセージを表示してプログラムを終了します
    exit()

# 予約日が有効かどうかを確認します
if not (1 <= reservation_date <= 30):
    print("Invalid reservation date. Exiting the program.")
    exit()

# 年齢がイベントの年齢制限を満たしているかを確認します
if events[event_code]["age_limit"] is not None and age < events[event_code]["age_limit"]:
    print("Age restriction: You cannot make a reservation for this event.")
# 日付制限がある場合、予約日が制限に合致しているかを確認します
elif events[event_code]["date_restrictions"] == "even" and reservation_date % 2 != 0:
    print("Date restriction: Your reservation could not be made on the selected date.")
elif events[event_code]["date_restrictions"] == "multiple_of_7" and reservation_date % 7 != 0:
    print("Date restriction: Your reservation could not be made on the selected date.")
else:
    print("Your reservation has been completed╰(*°▽°*)╯")