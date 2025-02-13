n = int(input())
array = [0] * 10001

for i in input().split():
    array[int(i)] = 1

m = int(input)
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes')
    else:
        print("no")


