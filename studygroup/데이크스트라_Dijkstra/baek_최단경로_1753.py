import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())

son = int(input()) #시작정점1

graph = [[] for _ in range(V+1)]
dis = [float('inf')]*(V+1) #답이 될 거리
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
#print(graph) [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]

q = []
heapq.heappush(q, (0, son))

dis[son] = 0

while q:
    d, node = heapq.heappop(q)
    # print('distance',distance,'node',node)
    if d > dis[node]:
        continue
    else:
        for i in graph[node]:
            we = d + i[1] #새로 갱신하는 거
            if we < dis[node]: #만약에 갱신한 게 원래꺼보다 더 작으면
                dis[v[0]] = we
                heapq.heappush(q, (we, i[0]))
                # print('q', q)
                # print('dis', dis)

for i in range(1, V+1):
    if dis[i] == float('inf'):
        print('INF')
    else:
        print(dis[i])

