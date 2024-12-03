# a부터 b까지 정수의 합 구하기 1

a = int(input("a값: "))
b = int(input("b값: "))

if a > b:
    a, b =  b, a

sum = 0

for i in range (a, b+1):
    if i < b:
        print(f"{i} +", end = " ")
    else:
        print(f"{i} = ", end = " ")
    sum += i

print(sum)