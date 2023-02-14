N, M = map(int,input().split()) # 4 2
arr = [0]*N
for i in range(N):
    arr[i] = i+1 #[1,2,3,4]
m = 1
for i in range(N, N-M, -1):
    m *= i

for i in range(m):
    pass
arr[0] arr[1]
arr[0] arr[2]
arr[0] arr[3]
arr[1] arr[0]
arr[1] arr[2]
arr[1] arr[3]