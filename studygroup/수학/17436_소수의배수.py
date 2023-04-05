import sys
input = sys.stdin.readline
N, M = map(int,input().split()) #1 100
arr = list(map(int,input().split())) #3
ans = []

for i in arr:
    for j in range(1, M+1):
        if (j not in ans) and (j % i == 0):
            ans.append(j)
print(len(ans))