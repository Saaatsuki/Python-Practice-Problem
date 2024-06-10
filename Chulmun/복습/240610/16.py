import random

# 3개의 고유한 랜덤 숫자 생성
pc_sel_set = set()
while len(pc_sel_set) < 3:
    pc_sel_num = random.randint(0, 9)
    pc_sel_set.add(pc_sel_num)
pc_sel_li = list(pc_sel_set)
print(pc_sel_li)  # 디버깅을 위해 출력, 최종 버전에서는 제거 가능

game_count = 0
strike = 0
ball = 0
out = 0

# 게임 루프
while strike < 3 and out < 3 and game_count < 5:
    game_count += 1
    strike = 0
    ball = 0
    
    # 입력 처리
    num1, num2, num3 = map(int, input(f"시도 {game_count} : 입력한 숫자 (세 개의 숫자를 공백으로 구분하여 입력) - ").split())
    input_num_li = [num1, num2, num3]
    
    strike_msg = ""
    ball_msg = ""
    out_msg = ""
    
    for i in range(3):
        if pc_sel_li[i] == input_num_li[i]:
            strike += 1
        elif input_num_li[i] in pc_sel_li:
            ball += 1
    strike_msg = f"{strike} Strike"
    ball_msg = f", {ball} Ball"
    if strike == 0 and ball == 0:
        out += 1
        out_msg = f", {out} Out" if out != 0 else ""
    
    print(f"결과 : {strike_msg}{ball_msg}{out_msg}")

if strike >= 3:
    print(f"게임 종료 : 승리\n정답 : {' '.join(map(str, pc_sel_li))}")
elif game_count >= 5:
    print(f"게임 종료 : 패배 (시도 횟수 {game_count}회 초과)\n정답 : {' '.join(map(str, pc_sel_li))}")
else:
    print(f"게임 종료 : 패배 (out {out}회 초과)\n정답 : {' '.join(map(str, pc_sel_li))}")