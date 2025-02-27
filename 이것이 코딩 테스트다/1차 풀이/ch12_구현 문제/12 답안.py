def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥이면
            # 바닥 위거나, '보의 한쪽 끝부분 위'거나, '다른 기둥 위' 라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 불가능

        elif stuff == 1: #설치된 것이 보라면
            # 왼쪽 끝부분이 기둥 위거나, 오른쪽 끝부분이 기둥 위거나, 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y-1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:

        x, y, stuff, operate = frame

        if operate == 0: # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])

        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
                
    return sorted(answer)