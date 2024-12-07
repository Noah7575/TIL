# 1부터 12까지, 8 제외하고 출력

for i in range(1, 13):
    if i == 8:
        continue
    # 반복문마다 판단을 거치므로 비효율적
    print(i, end = ' ')

print()