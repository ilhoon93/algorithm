from itertools import combinations
data = []
for i in range(9):
    data.append(int(input()))
result = []
for comb in list(combinations(data,7)):
    if sum(list(comb)) == 100:
        result = list(comb)
        break
result.sort()
for x in result:
    print(x)
