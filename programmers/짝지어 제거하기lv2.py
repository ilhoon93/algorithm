from collections import deque

def solution(s):
    answer = 0
    # 비교를 위한 deque 2개 선언
    a = deque()
    b = deque(s)
    
    while len(b)>0:
        aLength = len(a)
        
        # a가 비어있다면 b의 요소 입력
        if aLength == 0:
            a.append(b.popleft())
            
        else:
            # a의 마지막 요소와 b의 첫번쨰 요소 비교
            # 같으면 둘다 제거
            if a[-1] == b[0]:
                a.pop()
                b.popleft()
            else:
                a.append(b.popleft())
                
    if len(a) == 0:
        answer = 1 

    return answer