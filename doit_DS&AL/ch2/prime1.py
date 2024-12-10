# 1000 이하 소수 나열

counter = 0

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:
            break
    
    else:
        print(n)

print(f"나눗셈 횟수: {counter}")