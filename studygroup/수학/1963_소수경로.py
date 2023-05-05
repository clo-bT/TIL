import sys
from collections import deque
input = sys.stdin.readline
T = int(input())#3

def sosu():
    for i in range(2, 100):
        if arr[i]:
            for j in range(2*i,10000,i):
                arr[j] = False
                


def bfs():
    visited = [0 for _ in range(10000)]
    visited[S] = 1
    Q = deque()
    Q.append([S, 0])
    
    while Q:
        N, cnt = Q.popleft()
        N = str(N)
        if N == E:
            return cnt
        for i in range(4):
            for j in range(10):
                temp = int(N[:i] + str(j) + N[i+1:])
                if visited[temp] == 0 and temp>=1000 and arr[temp] == 1:
                    visited[temp] = 1
                    Q.append([temp,cnt+1])
                    
arr = [True for _ in range(10000)]
sosu()
for _ in range(T):
    S, E = map(int,input().split())
    print(bfs())
    
