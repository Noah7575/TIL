# a부터 b까지 정수의 합 구하기 2

a = int(input("a값: "))
b = int(input("b값: "))

if a > b:
    a, b =  b, a

sum = 0

for i in range(a, b):
    print(f"{i} +", end = '')
    sum += i

print(f"{b} = ", end ='')
sum += b

print(sum)