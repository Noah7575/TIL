"""
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
    -> 빗변 == 제일 긴 변
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 
    -> 몇 개인지 모르니까 무한루프문
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
    -> 리스트로 더 깔끔하게 풀 수 있다.
    -> max로 제일 긴 변 뽑아내고, remove로 나머지 변만 남기면 된다
"""

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if (a == 0 and b ==0 and c == 0):
        break

    # 빗변찾기
    if (a > b and a > c): 
        side = a
        s1 = b
        s2 = c

    if (b > a and b > c):
        side = b
        s1 = a
        s2 = c

    if (c > a and c > b):
        side = c
        s1 = a
        s2 = b

    if (side ** 2 == s1 ** 2 + s2 ** 2):
        print("right")
    else:
        print("wrong")

