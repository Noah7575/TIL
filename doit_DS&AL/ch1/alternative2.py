# +와 -를 번갈아 출력하기1

n = int(input("몇 개를 출력할까요?: "))

for i in range(n // 2):
    print("+-", end = '')

if n % 2 :
    print('+', end = '')

