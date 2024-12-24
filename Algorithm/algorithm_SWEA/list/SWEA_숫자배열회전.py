T = int(input()) #10
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [input().split() for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))
    # arr_t = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    a1 = [[0]*N for _ in range(N)]  # 90도 집어넣을 빈 리스트
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    print(f'#{tc}')
    for a,b,c in zip(a1,a2,a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')
