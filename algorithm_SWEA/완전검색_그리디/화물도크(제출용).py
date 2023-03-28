T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #10
    arr = []
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append([s, e])
    arr.sort(key= lambda x : (x[1], x[0])) #종료시간 기준 정렬
    # print(arr)
    # [[1, 4], [6, 15], [6, 15], [15, 16], [2, 19], [1, 22], [14, 23], [21, 23], [12, 24], [20, 24]]
    A = [arr[0]] #[1, 4]
    f = A[0][1] #4
    for i in range(1, N):
        if f <= arr[i][0]:
            A.append(arr[i])
            f = arr[i][1]
    print(f'#{tc} {len(A)}')