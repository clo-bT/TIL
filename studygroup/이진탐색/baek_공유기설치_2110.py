N, C = map(int,input().split())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort() #[1, 2, 4, 8, 9]
s,e = 0, arr[-1]
cnt = 1 
while (s-e) != 1:
    wid = (s + e) // 2  #너비
    for i in arr:
        if i == wid:
            s = wid
        else:
            