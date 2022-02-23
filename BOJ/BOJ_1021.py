from collections import deque
N, M = map(int, input().split())

data = deque([i+1 for i in range(N)])
target = list(map(int, input().split()))

cnt = 0
for num in target:
    while True:
        if data[0] == num:
            data.popleft()
            break
        idx = data.index(num)
        if abs(idx-0) <= (len(data) - idx):
            data.append(data.popleft())
            cnt += 1
        else:
            data.appendleft(data.pop())
            cnt += 1
print(cnt)
