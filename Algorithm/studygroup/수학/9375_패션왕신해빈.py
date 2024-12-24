T = int(input())#2
for tc in range(1, T+1):
    N = int(input())#3
    dic = {}
    for _ in range(N):
        name, clothes = input().split()
        if clothes in dic:
            dic[clothes].append(name)
        else:
            dic[clothes] = [name]
    cnt = 1
    for i in dic:
        cnt *= len(dic[i]) + 1
    print(cnt-1)


'''
t = int(input())

for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)
'''