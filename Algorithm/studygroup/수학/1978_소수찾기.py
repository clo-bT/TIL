N = int(input()) #4
arr = list(map(int,input().split())) #[1, 3, 5, 7]
ans = 0
for i in arr:
    cnt = 0
    if i>1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        if cnt == 0:
            ans += 1
print(ans)