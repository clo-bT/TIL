T = int(input()) #3
for tc in range(1,T+1):
    N, M = map(int,input().split()) # 4 5
    # print(N,M)
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    mx = 0
    mx_t = 0
    cnt = 0
    # cnt = N * ((M-1)//2 + 1)        # 심은 나무 개수
    for i in range(N):
        for j in range(0,M,2):
            cnt += 1
            ans += arr[i][j]
            if arr[i][j] > mx: # 최대값과 그때의 열 갱신
                mx = arr[i][j]
                mx_t = j
            elif arr[i][j] == mx and mx_t < j:
                mx = arr[i][j]
                mx_t = j

    print(f'#{tc} {ans} {cnt} {mx} {mx_t+1}')