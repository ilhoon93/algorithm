from itertools import combinations
n = int(input())
S = []
people = []
for i in range(n):
    people.append(i+1)
    S.append(list(map(int, input().split())))
    
diff = 987654321

for comb in list(combinations(people, n//2)):
    teamA = list(comb)
    teamB = []
    scoreA = 0
    scoreB = 0
    for x in people:
        if x not in teamA:
            teamB.append(x)
            
    for a in list(combinations(teamA, 2)):
        i = a[0]-1
        j = a[1]-1
        scoreA = scoreA + S[i][j] + S[j][i]
        #print(a, S[i][j], S[j][i], scoreA)
              
    for b in list(combinations(teamB, 2)):
        i = b[0]-1
        j = b[1]-1
        scoreB = scoreB + S[i][j] + S[j][i]
        #print(b, S[i][j], S[j][i], scoreB)
    
    diff = min(abs(scoreA - scoreB), diff)
    #print(scoreA, scoreB, "차이", diff)
print(diff)
