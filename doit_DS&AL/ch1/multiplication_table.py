# 구구단 곱셈표 출력

print('-' * 27)

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:3}", end = '')
        # :n은 n 자리로 출력하기
    print()
              
print('-' * 27)