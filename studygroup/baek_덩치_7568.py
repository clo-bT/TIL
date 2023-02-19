T = int(input()) #5
arr = []
result = [1] * T
for tc in range(T):
    a = list(map(int,input().split()))
    arr.append(a)
    # FEEDBACK
    # append가 시간이 더 걸림 [list(map(int, input().split())) for _ in range(N)]로 받기 !!
for i in range(T):
    for j in range(T):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            result[i] += 1
print(*result)

    
