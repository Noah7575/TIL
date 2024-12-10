counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else: # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n # 소수로 배열에 등록
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f"나눗셈 실행 횟수: {counter}")