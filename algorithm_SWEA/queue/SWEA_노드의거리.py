def bfs(s,g,N):
    visited = [0]*(N+1)
    queue = [s]
    visited[s] = 1
    while queue:
        t = queue.pop(0)

        for a in adjL[t]:
            if visited[a] == 0:
                queue.append(a)
                visited[a] = visited[t] + 1
    if visited[g] == 0:
        return 0
    else:
        return visited[g] -1


T = int(input()) #3
for tc in range(1, T+1):
    V, E = map(int,input().split()) # 6 5
    arr = [list(map(int,input().split())) for _ in range(E)]
    # arr = [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    S, G = map(int,input().split()) # 1 6

    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    print(f'#{tc}',bfs(S,G,V))