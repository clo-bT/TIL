di = [0, 1, 0, -1] #우 하 좌 상
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dir = 0 # 진행방향
    i = j = 0 # 숫자를 쓸 칸의 인덱스
    for k in range(1, N*N+1):
        arr[i][j] = k
        ni, nj = i + di[dir], j + dj[dir] # 다음 숫자를 쓸 좌표
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 : # 숫자를 쓸 수 있으면
            i, j = ni, nj
        else: # 배열을 벗어나거나 이미 숫자가 있으면
            dir = (dir+1) % 4 # 다음 방향으로 전환
            i, j = i+di[dir], j+dj[dir]
    print(f'#{tc}')
    for x in arr:
        print(*x)