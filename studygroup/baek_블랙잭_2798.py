N, M = map(int,input().split()) #5,21
arr = list(map(int,input().split())) #[5,6,7,8,9]
sum_arr = []
for i in range(N-2):
    for j in range(1,N-1):
        for r in range(2,N):
            if i+j <= N-1 and i+r <= N-1:
                sum_int = arr[i] + arr[i+j] + arr[i+r]
                if sum_int <= M:
                    sum_arr.append(sum_int)
print(max(sum_arr))