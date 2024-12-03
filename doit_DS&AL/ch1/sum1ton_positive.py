# 1부터 n까지 합 구하기: n은 양수만 입력

while True:
    n = int(input("n값:"))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n+1):
    sum += i

print(f"1부터 {n}까지 합: {sum}")