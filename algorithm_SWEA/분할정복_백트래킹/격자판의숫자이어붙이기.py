def dfs(n, a, i, j):
    if n == 7:
        if a not in lst:
            lst.append(a)
        return
    for di, dj in ((0,-1),(0,1),(-1,0),(1,0)):
        if 0<=i+di<4 and 0<=j+dj<4:
            dfs(n+1, a+arr[i+di][j+dj],i+di,j+dj)
    

T = int(input()) #1
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    lst = []
    for i in range(4):
        for j in range(4):
            dfs(1,arr[i][j], i, j)
    
    print(f'#{tc} {len(lst)}')
    