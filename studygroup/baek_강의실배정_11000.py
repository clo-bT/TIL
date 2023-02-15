N = int(input()) #3
ans = N
arr = []
for _ in range(N):
    S, T = map(int,input().split()) # 1 3, 2 4, 3 5
    arr.append([S,T])
for i in range(N):
    for j in range(N):
        if arr[i][0] == arr[j][1]:
            ans -= 1
print(ans)