N = int(input())
exs = list(map(str, input()))
stack = []
dic = {}

for i in range(N):
    dic[i + 65] = int(input())

for i in range(len(exs)):
    x = exs[i]
    
    if ord(x) >= 65 and ord(x) <= 90:
        stack.append(dic[ord(x)])
    else:
        tmpVal = 0
        if x == '+':
            tmpVal = stack[-2] + stack[-1]
        elif x == '-':
            tmpVal = stack[-2] - stack[-1]
        elif x == '*':
            tmpVal = stack[-2] * stack[-1]
        elif x == '/':
            tmpVal = stack[-2] / stack[-1]
        stack = stack[:-2]
        stack.append(tmpVal)
c = "{:.2f}".format(round(stack[0],2))
print(c)