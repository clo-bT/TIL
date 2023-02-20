sub = 1
cnt = 0
for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int,input().split()))
    while True:
        if arr[0]//10 == 0:
            arr.append(arr.pop(0))
            cnt += 1
        else:
            arr[0] -= sub % 5
            arr.append(arr.pop(0))
            sub += 1
        for i in range(8):
            arr[i]
    print(arr)
    

