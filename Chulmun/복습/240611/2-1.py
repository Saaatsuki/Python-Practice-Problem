mxm = int(input("토지의 면적을 제곱미터(㎡) 단위로 입력하세요 : "))
while not mxm>=0:
    mxm = int(input("잘못된 입력입니다.0이상의 숫자를 토지의 면적을 제곱미터(㎡) 단위로 입력하세요 : "))
ft = mxm * 10.7639
ac = mxm / 4046.86
print(f"{mxm:.2f} 제곱미터는 {ft} 평방피트입니다.\n{mxm:.2f} 제곱미터는 {ac} 에이커입니다.")