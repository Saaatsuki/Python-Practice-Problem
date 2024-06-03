while True:
    # メニューを表示
    print("-------------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-------------------------")

    # メニュー選択を受け付ける
    menu = input("메뉴를 선택하세요(1 or 2): ")

    # '1'を選択した場合
    if menu == '1':
        # 2から9までの数を入力させる
        while True:
            dan = input("구구단의 단을 입력하세요(1~9): ")

            # 入力が2~9の間の数字かをチェック
            if dan.isdigit() and 1 <= int(dan) <= 9:
                dan = int(dan)
                break  # 正しい入力なのでループを抜ける
            else:
                print("오류: 1부터 9까지의 정수를 입력하세요.")

        # 正しいダンを入力した場合、九九を出力する
        print(f"{dan}단 출력:")
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan*i}")

    # '2'を選択した場合
    elif menu == '2':
        print("프로그램을 종료합니다.")
        break

    # 不正な入力の場合
    else:
        print("오류: 1 또는 2만 입력하세요.")
