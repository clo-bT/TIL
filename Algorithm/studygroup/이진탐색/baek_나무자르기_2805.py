N, M = map(int,input().split()) #4 7 
arr = list(map(int,input().split())) #[20, 15, 10, 17]
s, e = 0, max(arr)
while s-e != 1:
    a = 0
    mid = (s + e)//2
    for i in arr:
        if i > mid:
            a += i-mid
    if a < M:
        e = mid-1
    else:
        s = mid+1
        ans = mid
print(ans)