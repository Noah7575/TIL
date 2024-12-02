import sys

a = sys.stdin.readline().strip()
print(ord(a))

# a 값을 input으로 받았을 때 백준에서 오류가 발생함
# sys의 readline()은 input()과 달리 한 번에 값을 읽어 버퍼에 저장함
# 그래서 훨씬 빠르고 오류도 안 나지만, 개행 문자가 포함됨
# strip()은 white space를 제거하는 함수이므로 함께 사용함
# 여러개 입력받기
    # a, b = map(int, sys.stdin.readline().strip()) 