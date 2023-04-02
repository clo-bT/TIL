## 승우님 코드

T = int(input())
 
def backtracking(x, y, distance, count):
    global result
    if result < distance:
        return
    if count == N:
        result = min(result, distance+abs(x - house[0])+abs(y - house[1]))
        return
 
    for i in range(N):
        if not visited[i]:
            nx, ny = customer[i]
            visited[i] = True
            backtracking(nx, ny, distance + abs(x - nx) + abs(y - ny), count+1)
            visited[i] = False
 
 
 
for tc in range(1, T+1):
    N = int(input())
    dummy = list(map(int, input().split()))
    company = dummy[:2]
    house = dummy[2:4]
    customer = list()
    for i in range(4, N*2+4, 2):
        customer.append([dummy[i], dummy[i+1]])
    # print(customer)
    visited = [False for _ in range(N)]
    result = 1234567890
    backtracking(company[0], company[1], 0, 0)
    print(f'#{tc}', result)
    
    
    
# 또 다른 풀이
T = int(input())
 
 
def backtracking(x, y, distance, count):
    global result
    if result < distance:
        return
    if count == N:
        result = min(result, distance+abs(x - dummy[2])+abs(y - dummy[3]))
        return
 
    for i in range(4, N*2 + 4, 2):
        if not visited[i]:
            nx, ny = dummy[i], dummy[i+1]
            visited[i] = True
            backtracking(nx, ny, distance + abs(x - nx) + abs(y - ny), count+1)
            visited[i] = False
 
 
for tc in range(1, T+1):
    N = int(input())
    dummy = list(map(int, input().split()))
    visited = [False for _ in range(N*2 + 4)]
    result = 1234567890
    backtracking(dummy[0], dummy[1], 0, 0)
    print(f'#{tc}', result)
    
    
## 병국님 코드
def f(i,k):
    global n,minV
    if i == k:
        s = 0
        for bb in range(n+1):
            s += abs(p[bb][0]-p[bb+1][0])+abs(p[bb][1]-p[bb+1][1])
        if minV > s:
            minV = s
 
    else:
        for j in range(1, k+1):
            if used[j] == 0:
                used[j] = 1
                p[i] = house[j]
                f(i+1,k)
                used[j] = 0
 
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    start = (arr[0],arr[1])
    end = (arr[2],arr[3])
    house = [start]
    p = [start] + [0] * n
    p.append(end)
    used = [1] + [0] * n + [1]
    minV=100000
    for x in range(4, (n+2)*2, 2):
        house.append((arr[x],arr[x+1]))
    house.append(end)
    f(1,n+1)
    print(f'#{tc} {minV}')