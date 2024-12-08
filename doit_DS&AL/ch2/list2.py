# 리스트 원소를 enumerate()로 스캔
    # enumerate()는 인덱스와 원소를 짝지어 튜플로 꺼낸다

x = ['john', 'george', 'paul', 'ringo']

for i, name in enumerate(x):
    print(f"x[{i}] = {name}")

for i, name in enumerate(x, 1): # 1부터 카운트하기
    print(f"{i}번째 = {name}")