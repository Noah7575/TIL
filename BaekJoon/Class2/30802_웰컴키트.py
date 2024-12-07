import sys

N = int(sys.stdin.readline().strip())
size = list(map(int, sys.stdin.readline().split()))

T, P = map(int, sys.stdin.readline().split())

# 티셔츠 묶음수
shirts_result = 0

for i in range(6):
    if (size[i] % T == 0):
        shirts_result += (size[i] // T)
    else:
        shirts_result += (size[i] // T + 1)

print(shirts_result)

# 펜: 몫과 나머지
print(f"{N // P} {N % P}")