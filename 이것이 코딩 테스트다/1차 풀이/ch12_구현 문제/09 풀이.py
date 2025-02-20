import sys
input = sys.stdin.readline

def solution(s):
    length = len(s)
    count_list = [9999] * (length + 1)
    
    for jump in range(1, length + 1):
        index = 0
        count = 1
        temp_abb = []
        while index + jump < length:
            if s[index : index + jump] == s[index + jump : index + (jump * 2)]:
                count += 1
                index += jump
            else: # 다음 블럭과 다르다면
                if count > 1:
                    temp_abb.append(str(count))
                    temp_abb.append(s[index : index + jump])
                    index += jump
                    count = 1
                elif count == 1:
                    temp_abb.append(s[index : index + jump])
                    index += jump
        
        count_list[jump] = len(temp_abb)

    answer = min(count_list)
    return answer

sentence = list(input().strip())

result = solution(sentence)
print(result)
