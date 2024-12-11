from ssearch_while import seq_search

print("실수검색, end 나오면 종료")

number = 0
x = []

while True:
    s = input(f"x[{number}]: ")
    if s == 'end':
        break
    x.append(float(s))
    number += 1

ky = float((input("검색할 키 : ")))

idx = seq_search(x, ky)
if idx == -1:
    print("없음")
else:
    print(f"검색값 좌표: x[{idx}]")