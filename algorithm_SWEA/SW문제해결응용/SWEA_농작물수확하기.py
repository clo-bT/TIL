T = int(input()) #1
for tc in range(1,T+1):
    N = int(input()) #5
    arr = [input() for _ in range(N)]
    # print(arr) #[['14054'], ['44250'], ['02032'], ['51204'], ['52212']]
    m = N//2
    ans = 0
    for i in range(N):
        for j in range(abs(m-i),N-abs(m-i)):
            ans += int(arr[i][j])
    print(f'#{tc}',ans)