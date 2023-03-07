import sys
input = sys.stdin.readline
N, M = map(int,input().split()) #4 2
tree = [[0, 1]]
if M == 2:
    for i in range(1,N-1):
        tree.append([i,i+1])
else:
    for i in range(2,M+1):
        tree.append([1,i])
    for i in range(M,N-1):
        tree.append([i,i+1])
for i in tree:
    print(*i)
'''
# 구글링
import sys
input = sys.stdin.readline 
n,m = map(int,input().split()) #4 3
node = 0
cnt = m - 1
for i in range(1, n):
    if m == 2:
        print(node,i)
        node += 1
    else:
        print(node,i)
        node += 1
        if cnt:
            node -= 1
            cnt -= 1


# 또 다른 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) #4 3
# 리프의 개수
leaf = 0
if m == 2:
    leaf = 1  # 중심 노드를 리프로 포함
 
last_leaf = 0
for i in range(1, n):
    if m > leaf:
        print(0, i)
        leaf += 1
    else:
        print(last_leaf, i)
    last_leaf = i




# 하드코딩
n, m = map(int, input().split())
 
if m == 2:
    for i in range(n - 1):
        print(i, i + 1)
 
else: # m이 3 이상
    print("0 1")
    for i in range(2, m + 1):
        print(1, i)
    for j in range(m, n - 1):
        print(j, j + 1)
'''