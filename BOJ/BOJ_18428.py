from itertools import combinations
n = int(input())
data = []
teachers = []
spaces = []
for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i,j))
        elif data[i][j] == 'X':
            spaces.append((i,j))
            
# 학생찾는 함수
def search(i, j):
    isStudent = False
    # 상
    for k in range(i,-1,-1):
        if data[k][j] == 'O':
            break
        elif data[k][j] == 'S':
            isStudent = True
            return isStudent
    # 하
    for k in range(i,n):
        if data[k][j] == 'O':
            break
        elif data[k][j] == 'S':
            isStudent = True
            return isStudent
    # 좌
    for k in range(j,-1,-1):
        if data[i][k] == 'O':
            break
        elif data[i][k] == 'S':
            isStudent = True
            return isStudent
    # 우
    for k in range(j,n):
        if data[i][k] == 'O':
            break
        elif data[i][k] == 'S':
            isStudent = True
            return isStudent
    return isStudent
def process():
    for t in teachers:
        if search(t[0], t[1]) == True:
            return True
    return False

result = ""
flag = False
for comb in combinations(spaces,3):
    # 장애물 설치
    for c in comb:
        i = c[0]
        j = c[1]
        data[i][j] = 'O'
    if process() == False:
        flag = True
        break
    else:
        # 장애물 해제
        for c in comb:
            i = c[0]
            j = c[1]
            data[i][j] = 'X'
if flag == True:
    result = "YES"
else:
    result = "NO"
        
print(result)
