
def f(i, j):
    if i == j:
        return i 
    else:
        m = (i+j)//2
        r1 = f(i,m)
        r2 = f(m+1,j)
        return win(r1,r2)
def win(a, b):
    if arr[a] - arr[b] == 1 or  arr[a] - arr[b] == -2:
        return a
    elif arr[a] - arr[b] == -1 or  arr[a] - arr[b] == 2:
        return b
    elif arr[a] - arr[b] == 0:
        return a

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #4 인원수
    arr = list(map(int,input().split()))
    print(f'#{tc}',f(0, N-1)+1)