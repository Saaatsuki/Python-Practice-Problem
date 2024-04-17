# 投入時間と投入時のスコアを入力
admission_time, current_score = map(int, input("Please enter the player's admission time and current scoreo((>ω< ))o : ").split())

# 追加スコアの初期値を設定します
additional_score = 0

# 最終スコアの初期値を設定します
final_score = current_score

# 入場時間が85分を超えるかどうかを確認します
if admission_time <= 85:
    # 入場時間を5分増やし、追加スコアを2増やします
    admission_time += 5
    additional_score += 2
    
    # 最終スコアに追加スコアを追加します
    final_score += additional_score

# 最終スコアを出力します
print("The final score of the team is {}!!!(‾◡◝)".format(final_score))