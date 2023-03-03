'''
T = int(input()) #1
for tc in range(1, T+1):
    N, M = map(int,input().split()) #4 12
    for _  in range(M):
        j, i, a = map(int,input().split())
'''


## 박영준 교수님 코드
B = 1
W = 2
OP = [0, 2, 1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bd = [[0]*(N+2) for _ in range(N+2)]
    bd[N//2][N//2] = W
    bd[N//2][N//2+1] = B
    bd[N//2+1][N//2] = B
    bd[N//2+1][N//2+1] = W
    for _ in range(M):
        j, i, bw = map(int, input().split())
        # 각 방향으로 뒤집을 수 있는 경우 찾기
        bd[i][j] = bw
        for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
            ni, nj = i+di, j+dj
            tmp = []        # 다른 색 돌의 좌표
            while bd[ni][nj] == OP[bw]:
                tmp.append((ni, nj))
                ni, nj = ni+di, nj+dj
            if bd[ni][nj] == bw:    # 놓은 돌과 같은 색을 만나서 중단된 경우
                for p, q in tmp:
                    bd[p][q] = bw
    bcnt = wcnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if bd[i][j]==B:
                bcnt += 1
            elif bd[i][j]==W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')





### 유튜브 교수님 코드
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # arr 네방향 0으로 패딩해서 둘러쌈
    arr = [[0]*(N+2) for _ in range(N+2)]
    # [1] 초기 돌 위치 놓기
    m = N//2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1
 
    # [2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향 처리
        for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            # 해당 방향으로 뻗어나가면서 처리
            tlst = []
            for mul in range(1, N):
                ni, nj = si+di*mul, sj+dj*mul
                if arr[ni][nj]==0:      # 빈칸 범위밖..
                    break
                elif arr[ni][nj] != d:  # 다른돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni,nj))
                else:                   # 같은돌=>후보들을 뒤집고, 종료
                    while tlst:
                        ti,tj = tlst.pop()
                        arr[ti][tj]=d
                    break
 
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{test_case} {bcnt} {wcnt}')