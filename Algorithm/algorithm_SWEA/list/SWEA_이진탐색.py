def binarySearch(l, p, key):
    cnt  = 0
    while l <= p:
        c = int((l + p) // 2)
        if c == key:
            return cnt
        elif c > key:
            p = c
        else:
            l = c
        cnt += 1

T = int(input()) #3
for tc in range(1, T+1):
    p, pa, pb = map(int,input().split()) #400,300,350
    cnt_a = binarySearch(1,p,pa)
    cnt_b = binarySearch(1,p,pb)
    if cnt_a < cnt_b:
        print(f'#{tc} A')
    elif cnt_a > cnt_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')