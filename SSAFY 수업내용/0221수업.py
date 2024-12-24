def bfs(v, N):
    visited = [0] * (N+1)                       # visited 생성
    q = [v]                                     # Q 생성
                                                # 시작점 인큐
    visited[v] = 1                              # 시작점 인큐 표시
    while q :                                   # 큐가 비어있지 않으면
        t = q.pop(0)                            # 디큐
        print(t, end=' ')                       # t에서 처리할일
        for v in adjL[t]:                       # t에 인접이고 방문한적 없는 v
            if visited[v] == 0:
                q.append(v)                     # v 인큐
                visited[v] = visited[t] + 1     # v인큐되었음을 표시

V, E = map(int,input().split())
arr = list(map(int,input().split()))
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)                         # 양방향이라서 둘 다 해줘야돼
    adjL[n2].append(n1)

bfs(1,V)                                        # 시작정점 1, v 마지막 정점