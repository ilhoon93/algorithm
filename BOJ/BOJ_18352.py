from collections import deque

n, m, k, x = map(int, input().split())
graph = []
check = []
for i in range(n+1):
    graph.append([])
    check.append(-1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append(x)
check[x] = 0
while q:
    v = q.popleft()
    for i in graph[v]:
        if check[i] == -1:
            q.append(i)
            check[i] = check[v] + 1

cnt = 0
for i in range(n+1):
    if check[i] == k:
        cnt += 1
        print(i)
if cnt == 0:
    print(-1)
