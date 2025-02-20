def solution(s):
    length = len(s)
    if length == 1:  # 문자열이 한 글자인 경우, 압축이 불가능하므로 길이 1 반환
        return 1
    
    min_length = length  # 초기 최소 길이를 원래 길이로 설정

    # 압축할 단위 jump를 1부터 length//2까지 시도 (length 이상은 의미 없음)
    for jump in range(1, length // 2 + 1):
        compressed = ""
        prev = s[:jump]  # 첫 번째 블록 저장
        count = 1
        
        # jump 단위로 문자열을 순회하며 압축 진행
        for i in range(jump, length, jump):
            curr = s[i:i+jump]  # 현재 블록

            if prev == curr:  # 이전 블록과 같으면 카운트 증가
                count += 1
            else:
                if count > 1:
                    compressed += str(count) + prev  # 반복된 경우 숫자+문자 추가
                else:
                    compressed += prev  # 반복되지 않은 경우 그냥 추가
                
                prev = curr  # 현재 블록을 새로운 prev로 설정
                count = 1  # 카운트 초기화
        
        # 마지막 블록 처리
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        # 최소 압축 길이 갱신
        min_length = min(min_length, len(compressed))

    return min_length

sentence = input().strip()  # 리스트 변환 필요 없음
print(solution(sentence))