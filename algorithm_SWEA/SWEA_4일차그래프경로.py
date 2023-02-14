def f1(S, G, N):            # S출발 G도착 N마지막정점
    visited = [0] * (N+1)   # 방문표시
    stack = []              # 스택
    v = S
    while True:
        if v == G:
            return 1
        visited[v] = 1
        for w in range(1, N+1): # 인접하고 방문한한 w가 있으면
            if adjM[v][w] and visited[w] == 0:
                stack.append(v) # 현재 정점 push
                v = w # 인접으로 이동해
                break # 이동하고 나면 나가서 visited[v] = 1이라고 방문했다고 표시해줘
            else: #인접정점이 없고(갈 곳이 없으면) 스택에 뭔가 남아있으면
                if stack:
                    v = stack.pop() # 뒷걸음질 쳐. 하나씩 빼봐
                else: # 스택이 비어있으면
                    break
    return 0



T = int(input()) #3
arr = []

for tc in range(1, T+1):
    V, E = map(int,input().split()) #6 5
    adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬
    for _ in range(E): #E개의 줄에 걸쳐
        a, b = map(int,input().split())     # a출발, b도착 (유향그래프)
        adjM[a][b] = 1                      # a에 인접한 b
        # adjM[b][a] = 1                    # 무향그래프였다면 이 코드가 있어야돼. 유향이면 없어야돼
    S, G = map(int,input().split())
    # -------입력 끝 탐색하자---
    f1(S, G, V)


