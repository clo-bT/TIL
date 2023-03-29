
def sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left = arr[:m]
    right = arr[m:]
    left = sort(left)
    right = sort(right)

    i, j = 0, 0 # 왼쪽, 오른쪽 리스트 인덱스
    li = []    # 정렬한 거 저장할 리스트
    if left[-1] > right[-1]:
        cnt += 1
    while i < len(left) and j < len(right): # 인덱스가 list 개수보다 커지기 전까지
        if left[i] < right[j]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1
    while i < len(left):
        li.append(left[i])
        i += 1
    while j < len(right):
        li.append(right[j])
        j += 1
    return li


T = int(input())#3
for tc in range(1, T+1):
    N = int(input())#5
    arr = list(map(int,input().split()))
    tmp = [0]*N
    cnt = 0
    # msort(arr)
    ans = sort(arr)
    print(f'#{tc} {ans[N//2]} {cnt}')
