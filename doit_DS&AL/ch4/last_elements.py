# 원하는 개수만큼 값을 입력받고, 마지막 n개를 저장함

n = int(input("n="))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input(f"{cnt + 1}번째 정수: "))
    cnt += 1

    retry = input("retry? :")
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f"{i+1}번째: {a[i % n]}")
    i += 1
