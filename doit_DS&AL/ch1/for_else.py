# 난수생성, 13이 나오면 중단

import random

n = int(input("난수 개수: "))

for i in range(n):
    r = random.randint(10, 99)
    print(r, end = ' ')
    if r == 13:
        print('\n 프로그램 중단!')
        break
    # 13이 나오면 생성 중단
else:
    print("\n 난수 생성을 종료합니다.")
    # 13이 안 나오고 n개만큼 생성될 경우