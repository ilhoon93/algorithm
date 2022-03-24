# 거짓말
N, M = map(int, input().split())
tList = list(map(int, input().split()))
t = tList[0]
tList = set(tList[1:])
trueParties = []

for m in range(M):
    trueParties.append(False)
data = []
# 현재 파티
for m in range(M):
    pList = list(map(int, input().split()))
    p = pList[0]
    pList = pList[1:]
    data.append(pList)
    

while True:
    # 진실을 들어야하는 사람의 수
    cnt = len(tList)
  
    for m in range(M):
        pList = data[m]
        if trueParties[m] == False:
            for x in tList:
                if x in pList:
                    trueParties[m] = True
                    break
                    
        # 모든 파티원을 진실집합으로 추가
        if trueParties[m] == True:
            for x in pList:
                tList.add(x)
        
    if cnt == len(tList):
        break
        
result = 0
for i in range(M):
    if trueParties[i] == False:
        result += 1
        
print(result) 
