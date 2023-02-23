
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
    return
 
 
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    last = 0
    heap = [0] * (N+1)
    for item in arr:
        enq(item)
    
    ans = 0
    # 조상노드 합
    while last > 0:
        last = last//2
        ans += heap[last]
    print(f'#{tc}', ans)