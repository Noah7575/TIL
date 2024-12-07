# 직각삼각형 별찍기2

n = int(input("짧은 변의 길이: "))

for i in range(n):
    for _ in range(n - i -1):
        print("_", end = '')
    for _ in range(i+1):
        print("*", end = '')
    print()
    