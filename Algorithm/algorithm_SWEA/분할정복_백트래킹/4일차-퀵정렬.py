def partition(A, l, r):
    pivot = A[l]
    i, j = l, r     #i 가장 왼쪽에 있는 피봇보다 큰 값, j는 가장 오른쪽에 있는 작은값
    while i<=j:
        while i<=j and A[i]<=pivot:
            i += 1
        while i <= j and A[i] >= pivot:
            j -= 1
        if i<j:
            A[i], A[j] = A[j], A[i]     # 피봇보다 큰값이 작은값 왼쪽에 있는 경우 교환
    A[j], A[l] = A[l], A[j]             # 피봇 값을 경계에 위치시킴
    return j                            # 피봇의 위치를 리턴
def qsort(A, l, r):
    if l<r:
        s = partition(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

T = int(input())#3
for tc in range(1, T+1):
    N = int(input())#5
    arr = list(map(int,input().split()))
    qsort(arr,0,N-1)
    print(f'#{tc} {arr[N//2]}')
