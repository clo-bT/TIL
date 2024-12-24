'''
input
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

output
#1 3
#2 2
#3 3
'''

def findset(i):
    while rep[i] != i:
        i = rep[i]
    return i
def union(x, y):
    rep[findset(y)] = findset(x)
    # print(rep)
    # [0, 1, 1, 3, 4, 5]
    # [0, 1, 1, 3, 3, 5]

T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #5 2
    arr = list(map(int,input().split())) #[1, 2, 3, 4]
    rep = [i for i in range(N+1)] #[0, 1, 2, 3, 4, 5]

    for i in range(M):
        x, y = arr[2*i], arr[2*i+1]
        union(x, y)

    cnt = 0
    for i in range(1, N+1):
        if rep[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')