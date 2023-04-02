def f(i, n, c): # i:현재 교환횟수 n:주어진 교환횟수 c:카드수
    global maxV
    if i == n: # 남은 교환횟수가 없으면
        tmp = int(''.join(arr))
        if maxV < tmp:
             maxV = tmp
    else:
        for p in range(c-1):
            for q in range(p+1,c):
                arr[p], arr[q] = arr[q], arr[p]
                tmp = int(''.join(arr))
                if tmp not in v[i]: #이미 있는 거면 안넣고 없을 때만 넣기
                    v[i].append(tmp)
                    f(i+1, n, c) #다음 교환
                arr[p], arr[q] = arr[q], arr[p] #다른 p,q를 선택하기 위해 원상 복구

T = int(input()) #3
for tc in range(1, T+1):
    a, n = input().split()
    arr = list(a)
    n = int(n)

    maxV = 0
    v = [[] for _ in range(n)] #교환횟수 별로 만들어지는 숫자 저장
    f(0, n, len(arr))
    print(f'#{tc} {maxV}')

'''
input
3
123 1
2737 1
32888 2

output
#1 321
#2 7732
#3 88832
'''