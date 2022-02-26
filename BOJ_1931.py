n = int(input())
data = []
for _ in range(n):
    s, e = map(int, input().split())
    data.append((s,e))

data = sorted(data)
tmp = []
aligned_time = data[0][0]
cnt = 0
for x in data:
    if x[0] < aligned_time:
        # 1, 4가 0보다 작아서 안들어가네
        if (tmp[-1][1] - tmp[-1][0]) > (x[1] - x[0]) and x[1] <= tmp[-1][1]:
            tmp.pop()
            tmp.append((x[0], x[1]))
            aligned_time = x[1]
            continue
        else:
            continue
    if x[0] == x[1]:
        cnt += 1
    else:
        aligned_time = x[1]
        cnt += 1
        tmp.append((x[0], x[1]))

print(cnt)
