def f(b):
    global cnt
    l, r = 0, N-1
    while l <= r:
        m = (l + r) // 2
        if A[m] == b:
            cnt += 1
            break
        elif b < A[m]:
            if arr[-1] == 1:
                break
            r = m-1
            arr.append(1)
        elif A[m] < b:
            if arr[-1] == 0:
                break
            l = m+1
            arr.append(0)

T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 3 len(A) len(B)
    A = sorted(list(map(int,input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        arr = [2]
        f(b)
    print(f'#{tc} {cnt}')

'''
민석님 코드 일부
        if list[m] == target:
            cnt += 1
            break

        elif list[m] > target:
            if temp[-1] == 'left':  # 이전 탐색이 왼쪽인데 또 왼쪽
                break               # 실패
            e = m - 1
            temp.append('left')       # 왼쪽 탐색
        else:
            if temp[-1] == 'right':  # 이전 탐색이 오른쪽인데 또 오른쪽
                break
            s = m + 1
            temp.append('right')      # 오른쪽 탐색
'''