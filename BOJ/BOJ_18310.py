n = int(input())
data = list(map(int,input().split()))
data.sort()

N = len(data)
median = (N//2)
if N%2==0:
    median-=1
print(data[median])
