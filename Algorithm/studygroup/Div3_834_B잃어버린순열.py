T = int(input()) #5
for _ in range(T):
    m, s = map(int,input().split()) #3, 13
    a = list(map(int,input().split()))
    sum_i = 0
    for i in range(1, 50):
        sum_i += i
        if sum(a) + s == sum_i:
            print('Yes')
            break
        elif sum(a) + s < sum_i:
            print('No')
            break
        

