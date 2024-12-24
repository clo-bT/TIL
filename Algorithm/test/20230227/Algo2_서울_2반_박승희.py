T = int(input()) #3
for tc in range(1,T+1):
    N, K, A, B = map(int,input().split()) # 10 9 4 5
    arr = [list(input().split()) for _ in range(N)]
    u, d = A - K//2, A + K//2           # 탐색구간의 위쪽, 아래쪽
    l, r = B - K//2, B + K//2           # 탐색구간의 왼쪽, 오른쪽
    star = 0
    ans = []
    c = 0
    for i in range(N):                  # 별의 총 개수 세기
        for j in range(N):
            if arr[i][j] == '*':
                star += 1
    while u < d or l < r:
        cnt = 0
        for k in range(u, d+1):         # 위에서부터 아래 탐색
            for p in range(l, r+1):     # 왼쪽에서 오른쪽 탐색
                if 0<=k<K and 0<=p<K and arr[k][p] == '*':
                    cnt += 1
        if len(ans) == 0 and star != cnt:    # 확대 안 했는데 다 못 찍으면
            print(f'#{tc} -1')               # -1 출력
            break
        else:
            ans.append(cnt)
            u += 1
            d -= 1
            l += 1
            r -= 1
            c += 1
        if ans and star != cnt:
            print(f'#{tc} {c-2}')
            break
