import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon = dict()

for i in range(1, N+1):
    name = input().strip()
    pocketmon[i] = name

pocket_reversed = {v: k for k, v in pocketmon.items()}

for _ in range(M):
    quiz = str(input().strip())
    # quiz가 숫자인 경우
    if quiz.isdigit():
        quiz = int(quiz)
        print(pocketmon[quiz])
    # 이름인 경우
    elif quiz.isalpha():
        print(pocket_reversed[quiz])
