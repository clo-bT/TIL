N = int(input()) #5
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)