import sys

T = int(sys.stdin.readline().strip())

for i in range(T): 
    # 테스트케이스 개수만큼 반복하기
    temp = sys.stdin.readline().split()
    R = int(temp[0]) # 글자반복개수
    S = temp[1] # 반복대상 문자열

    for j in range(len(S)): 
        print(S[j] * R, end = '')
        
    print()
