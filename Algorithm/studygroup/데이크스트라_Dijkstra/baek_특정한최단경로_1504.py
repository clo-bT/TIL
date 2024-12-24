import sys
import heapq

input = sys.stdin.readline
N, E = map(int, input().split()) #4 6

graph = [[] for _ in range(E)]
dis = [float('inf')]*(N+1)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split()) #2 3