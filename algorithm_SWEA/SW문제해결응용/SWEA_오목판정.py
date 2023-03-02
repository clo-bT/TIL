T = int(input()) #4
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)] #['....o', '...o.', '..o..', '.o...', 'o....']
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                pass