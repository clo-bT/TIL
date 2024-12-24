'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

#1 2
#2 4
#3 10
'''

## 교수님 코드
def dijkstra(N):
    D = [0] * (N + 1)
    U = [0] * (N + 1)
    for i in range(N + 1):
        D[i] = adjM[0][i]

    for _ in range(N):
        minV = INF
        w = 0
        for i in range(N + 1):  # D[w] 최소인 w찾기
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1  # D[w]는 최소비용 확정
        for i in range(N + 1):
            if 0 < adjM[w][i] < INF:  # w에 인접인 i에 대해
                D[i] = min(D[i], D[w] + adjM[w][i])  # w를 거쳐 i로 가는 비용 비교
    return D[N]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N 마지막 정점번호, E 간선 수
    INF = 10000001
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adjM[i][i] = 0  # 자기 자신인 경우 비용 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w  # 인접한 경우 가중치

    print(f'#{tc} {dijkstra(N)}')


'''
## 연주언니 코드
def dijkstra(s,V): # s 출발, V 마지막 정점 번호
    U = [0]*(N+1)
    U[s] = 1 # 방문기록
    for i in range(N+1):
        D[i] = adjM[s][i] # 각 인접점과의 거리
 
    for _ in range(N): # 각 정점의 비용
        minV = INF
        w = 0
        for i in range(N+1):
            if U[i]==0 and minV > D[i]: # 방문안했고, 거리가 최소인 정점
                w = i # 정점번호 갱신
                minV = D[i] # 거리의 최소합 갱신
        U[w] = 1 # 최소비용 확정
        for v in range(N+1):
            if 0<adjM[w][v]<INF: # w에 인접인 v의 조건
                D[v] = min(D[v], D[w]+adjM[w][v])
 
INF = 11
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split()) # N 마지막 연결지점 번호, E 도로의 수
    adjM = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s,e,w = map(int, input().split()) # s 시작, e 끝 지점, w 거리
        adjM[s][e] = w
 
    D = [0]*(N+1)
    dijkstra(0,N)
    print(f'#{tc} {D[N]}')
'''