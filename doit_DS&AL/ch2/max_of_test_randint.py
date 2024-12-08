# 배열최댓값출력(랜덤)

import random
from max import max_of

print('난수 최댓값을 구합니다.')
num = int(input("난수 개수: "))
lo = int(input("난수 최솟값: "))
hi = int(input("난수 최댓값: "))

x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f"{(x)}")
print(f"최댓값: {max_of(x)}")