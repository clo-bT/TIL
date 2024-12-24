import sys
input = sys.stdin.readline
N = int(input()) #4
tree = [[] for _ in range(N+1)]
depth = [0]*(N+1)
visited = [0]*(N+1)
ans = 0
for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)   # tree[a] = b 랑 다름
    tree[b].append(a)
# print(tree) [[], [2], [1, 3, 4], [2], [2]]

def dep(a):
    visited[a] = 1
    for i in tree[a]:
        if visited[i] == 0:
            depth[i] = depth[a] + 1
            dep(i)

dep(1)
for i in range(2,N+1): #루트노드빼고
    if len(tree[i]) == 1:   # 리프노드
        ans += depth[i]
# print(depth) [0, 0, 1, 2, 2]
if ans % 2 == 0:
    print("No")
else:
    print("Yes")