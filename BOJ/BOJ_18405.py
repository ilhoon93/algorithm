from collections import deque
n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j, 0))
S, X, Y = map(int, input().split())
data.sort()
q = deque(data)


dx = [0, 0, -1, 1]
dy = [-1,1, 0, 0]
while q:
    
    v = q.popleft()
    k = v[0]
    i = v[1]
    j = v[2]
    s = v[3]

    if s == S:
        break
    
    for x in range(4):
        ni = i + dx[x]
        nj = j + dy[x]

        if ni >= n or ni < 0 or nj >= n or nj < 0:
                continue
        if graph[ni][nj] == 0:
            graph[ni][nj] = k
            q.append((k,ni,nj,s+1))
            

print(graph[X-1][Y-1])
