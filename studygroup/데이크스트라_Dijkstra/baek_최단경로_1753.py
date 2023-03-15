import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())

son = int(input()) #시작정점1

graph = [[] for _ in range(V+1)]
dis = [float('inf')]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
#print(graph) [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]

q = []
heapq.heappush(q, (0, son))

dis[son] = 0

while q:
    distance, node = heapq.heappop(q)
    # print('distance',distance,'node',node)
    if distance > dis[node]:
        continue
    else:
        for v in graph[node]:
            weight = distance + v[1]
            if weight < dis[v[0]]:
                dis[v[0]] = weight
                heapq.heappush(q, (weight, v[0]))
                # print('q', q)
                # print('dis', dis)

for i in range(1, V+1):
    if dis[i] == float('inf'):
        print('INF')
    else:
        print(dis[i])

