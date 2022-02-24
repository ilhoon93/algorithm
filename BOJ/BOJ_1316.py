N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    checker = [0 for i in range(ord('z')-ord('a')+1)]
    isGroup = True
    for i in range(len(word)):
        idx = ord(word[i])-97
        if checker[idx] == 0:
            checker[idx] = 1
        else:
            if word[i] == word[i-1]:
                continue
            else:
                isGroup = False
    if isGroup == True:
        cnt += 1
print(cnt)
