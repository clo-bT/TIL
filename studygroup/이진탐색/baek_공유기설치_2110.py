import sys
input = sys.stdin.readline

N, C = map(int,input().split()) #5 3
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort() #[1, 2, 4, 8, 9]
s,e = 0, arr[-1]
ans = arr[-1] - arr[0]
while s<=e:
    cnt = 1 
    wid = (s + e) // 2  # 너비
    start, end = arr[0], arr[-1]
    for i in range(N):
        if arr[i] - start >= wid:
            cnt += 1
            start = arr[i]
    if cnt >= C:
        s = wid + 1
        ans = wid
    else:
        e = wid - 1
print(ans)