def dfs(n, sm):
    global ans
    if ans <= sm:
        return
    if n > 12:
        ans = min(ans, sm)
        return
    dfs(n+1, sm+d*arr[n])
    dfs(n+1, sm+m)
    dfs(n+3, sm+m3)
    dfs(n+12, sm+y)

T = int(input())#10
for tc in range(1, T+1):
    d, m, m3, y = map(int,input().split())
    arr = [0]+list(map(int,input().split()))
    ans = 365*3000
    dfs(1, 0)
    print(f'#{tc} {ans}')