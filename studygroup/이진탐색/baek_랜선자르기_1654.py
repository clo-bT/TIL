K, N = map(int,input().split()) #4 11
arr = [0] * K
for i in range(K):
    arr[i] = int(input())
s, e = 1, max(arr) 
while s<=e:
    a = 0
    mid = (s+e)//2
    for i in arr:
        a += i//mid
    if a < N:
        e = mid - 1
    elif a >= N:
        s = mid + 1 
        ans = mid
print(ans)
