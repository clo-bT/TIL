def f(n):
    if n <= N:
        f(n*2)
        print(tree[n], end='')
        f(n*2+1)

for tc in range(1,11):
    N = int(input()) # 정점 수
    arr = [list(input().split()) for _ in range(N)]
    tree = ['']*(N+1)
    for i in range(1,N+1):
        tree[i] = arr[i-1][1]
    
    print(f'#{tc}', end=' '),f(1)
    print()
        
        
