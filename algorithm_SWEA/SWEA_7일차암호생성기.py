for _ in range(1, 11):
    sub = 0
    tc = int(input())
    arr = list(map(int,input().split()))
    while True:
        sub += 1
        if arr[0] //10 != 0:
            arr[0] = arr[0] - sub%5
            arr.append(arr.pop(0))
        if arr[-1] <= 0:
            arr[-1] = 0
            break
    print(arr)
