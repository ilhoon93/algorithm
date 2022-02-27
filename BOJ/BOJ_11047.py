n, k = map(int, input().split())
coin_type = []
for i in range(n):
    coin_type.append(int(input()))
coin_type = sorted(coin_type, reverse=True)

def calc(x, data, ans):
    global result
    cnt = x//data[0]
    remain = x%data[0]
    result = ans + cnt
    if remain == 0:
        return (ans + cnt)
    calc(remain, data[1:], ans+cnt)


calc(k, coin_type, 0)
print(result)
