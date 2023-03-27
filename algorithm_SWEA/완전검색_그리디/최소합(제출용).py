def f(i, j, N, s):
    global minV
    if i>=N or j>=N:    # 진입불가
        return
    elif i==N-1 and j==N-1: # 도착
        if minV > s + arr[i][j]:
            minV = s + arr[i][j]
    else:
        f(i, j + 1, N, s + arr[i][j])
        f(i + 1, j, N, s + arr[i][j])

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [list(map(int,input().split())) for _ in range(N)]
    minV = 1000
    f(0, 0, N, 0)
    print(minV)