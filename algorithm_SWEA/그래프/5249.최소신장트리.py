'''
3
2 3
0 1 1
0 2 1
1 2 6
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
#2 13
#3 22
'''

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x
def union(x,y):
    rep[find_set(y)] = find_set(x)



T = int(input()) #3
for tc in range(1, T+1):
    V, E = map(int,input().split()) # 0~V 정점번호, E 간선 수
    #makeset()
    rep = [i for i in range(V+1)]   # V번까지 각자 대표
    graph = []
    for _ in range(E):
        v1, v2, w = map(int,input().split())
        graph.append([v1, v2, w])
    # (1) 가중치 기준 정렬
    graph.sort(key=lambda x:x[2])

    # (2) N개 정점(V+1), N-1개의 간선 선택
    N = V + 1           # N개 정점
    s = 0               # MST에 포함된 간선의 가중치 합
    cnt = 0
    for u, v, w in graph: # 가중치가 작은 것부터
        if find_set(u) != find_set(v):  # 사이클이 생기지 않으면
            cnt += 1    # 간선 수 증가
            s += w      # 가중치 합
            union(u, v)
            if cnt == N - 1:            # MST 구성완료
                break
    print(f'#{tc} {s}')