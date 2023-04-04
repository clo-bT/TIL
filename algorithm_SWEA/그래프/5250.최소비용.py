'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1

#1 5
#2 8
#3 9
'''
## 방법1
def dij(N):
    INF = 100000000
    D = [[INF] * N for _ in range(N)]
    D[0][0] = 0  # 출발
    U = [[0] * N for _ in range(N)]
    U[0][0] = 1
    for _ in range(N * N - 1):
        # D[w]가 최소인 w 찾기
        minV = INF
        wi = wj = 0
        for i in range(N):
            for j in range(N):
                if U[i][j] == 0 and minV > D[i][j]:
                    minV = D[i][j]
                    wi, wj = i, j
        U[wi][wj] = 1  # D[w]는 최소비용 확정
        # w에 인접인 v에 대해
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = wi + di, wj + dj
            if 0 <= ni < N and 0 <= nj < N and U[ni][nj] == 0:
                cost = 1 + max(0, arr[ni][nj] - arr[wi][wj])
                D[ni][nj] = min(D[ni][nj], D[wi][wj] + cost)
    return D[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dij(N)}')


## 방법2
def f(N):
    INF = 100000000
    Q = []
    D = [[INF] * N for _ in range(N)]
    Q.append((0, 0))
    D[0][0] = 0
    while Q:  # 더이상 비용이 갱신되는 칸이 없을때까지 반복
        i, j = Q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and D[ni][nj] > (D[i][j] + 1 + max(0, arr[ni][nj] - arr[i][j])):
                D[ni][nj] = D[i][j] + 1 + max(0, arr[ni][nj] - arr[i][j])
                Q.append((ni, nj))
    return D[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {f(N)}')