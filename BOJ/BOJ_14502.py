from itertools import combinations
from copy import deepcopy

# 데이터 입력
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
cp_data = []
result = 0
# dfs
def dfs(i, j):
    cp_data[i][j] = 2
    dx = [0, 0, -1 ,1]
    dy = [-1, 1, 0, 0]
    
    for x in range(4):
        ni = i + dx[x]
        nj = j + dy[x]
        
        if ni >= n or ni < 0 or nj >= m or nj < 0:
            continue
            
        if cp_data[ni][nj] == 0:
            dfs(ni, nj)
    
# 세울 수 있는 벽 찾기
walls = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            walls.append((i,j))

for comb in list(combinations(walls, 3)):
    cp_data = deepcopy(data)

    for c in comb:
        ii = c[0]
        jj = c[1]
        cp_data[ii][jj] = 1

    # 바이러스 퍼트리기
    for i in range(n):
        for j in range(m):
            if cp_data[i][j] == 2:
                dfs(i, j)
    
    # 안전영역 개수세기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cp_data[i][j] == 0:
                cnt += 1
    if cnt > result:
        result = cnt
print(result)
