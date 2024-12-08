# 1부터 n 까지 정수의 합 구하기

def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input("x값: "))
print(f"1부터 {x}까지의 합: {sum_1ton(x)}")