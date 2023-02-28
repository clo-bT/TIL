T = int(input()) #10
li = [2,3,5,7,11]
for tc in range(1, T+1):
    cnt = [0] * (len(li))
    num = int(input())

    for i in range(len(li)):
        while num % li[i] == 0:
            cnt[i] += 1
            num //= li[i]
    print(f'#{tc}',*cnt)