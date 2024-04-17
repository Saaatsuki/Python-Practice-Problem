# 1. shopping_list라는 이름의 빈 리스트를 생성합니다.
shopping_list = []

# 2. 다음 품목들을 쇼핑 리스트에 추가하세요: 'milk', 'bread', 'eggs', 'apple'.
shopping_list.extend(['milk', 'bread', 'eggs', 'apple'])

# 3. print 함수를 사용하여 현재 쇼핑 리스트의 내용을 출력합니다. 
print("현재 쇼핑 리스트:", shopping_list)

# 4. 쇼핑을 시작하기 전에 'toilet paper'가 빠져 있는 것을 발견하고 리스트의 맨 앞에 추가합니다. 
shopping_list.insert(0, 'toilet paper')

# 5. 이번에는 'orange juice'를 리스트의 두 번째 위치에 추가하세요. 
shopping_list.insert(1, 'orange juice')

# 6. 마지막으로, 'chicken', 'rice'를 리스트에 추가해야 하는데, 이 두 품목을 한 번의 연산으로 리스트에추가하세요. (extend()함수 또는 ‘+’ 연산 사용)
shopping_list += ['chicken', 'rice']

# 7. 각 단계 후에 쇼핑 리스트를 출력하여, 추가된 품목들을 확인할 수 있게 합니다
print("최종 쇼핑 리스트:", shopping_list)