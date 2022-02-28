string = input()
n = len(string)
result = 0
def isPal(str):
    n = len(str)
    for i in range(n//2):
        if str[i] != str[n-i-1]:
            return False
    return True

for i in range(n):
    tmp = ''.join(reversed(string[0:i]))
    x = string + str(tmp)
    if isPal(x):
        print(len(x))
        break
