T = int(input()) #4
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    ans = "Possible"
    for i in range(N):
        bread = arr[i]//M *K-(i+1)
        if bread<0:
            ans = "Impossible"
            break
    print(f'#{tc}',ans)