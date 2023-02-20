T = int(input()) #3

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    queue = [0] * M
    rear = 0
    for i in range(M):
        rear += 1
        queue[i] = arr[rear % N]

    print(f'#{tc}', queue[-1])
