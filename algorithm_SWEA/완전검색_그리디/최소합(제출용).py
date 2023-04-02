def f(i, j, N, s):
    global minV
    if i>=N or j>=N:    # 진입불가
        return
    elif i==N-1 and j==N-1: # 도착
        if minV > s + arr[i][j]:
            minV = s + arr[i][j]
    else:
        f(i, j + 1, N, s + arr[i][j])
        f(i + 1, j, N, s + arr[i][j])

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [list(map(int,input().split())) for _ in range(N)]
    minV = 1000
    f(0, 0, N, 0)
    print(f'#{tc} {minV}')
    
'''
input
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1

output
#1 15
#2 18
#3 33
'''