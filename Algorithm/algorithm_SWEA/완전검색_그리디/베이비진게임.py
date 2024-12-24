'''
input
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3

output
#1 0
#2 1
#3 2
'''

## 상미언니 코드
def f(lst):
    global ans
    for i in range(len(lst)):
        if lst[i] >= 3:          # triplet
            ans = 1
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:     # run
            ans = 1
 
 
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    A = [0]*12
    B = [0]*12              # index range 맞춰주려고 2 더함
    ans = 0
    win = 0
    for i in range(6):
        A[arr[i*2]] += 1
        f(A)
        if ans:
            win = 1
            break
             
        B[arr[i*2+1]] += 1
        f(B)
        if ans:
            win = 2
            break
 
    print(f'#{t} {win}')
    
    
## 성원언니 코드
def run_triplet(lst, n):
    for i in range(n - 2):
        if lst[i] == lst[i+1] == lst[i+2]:  # triplet 인가?
            return True
        if lst[i]+1 in lst and lst[i]+2 in lst:     # run인가?
            return True
    return False
 
T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    a = []
    b = []
    ans = 0
    for i in range(0,12,2):
        a.append(lst[i])
        b.append(lst[i+1])
        if i >= 4:
            if run_triplet(sorted(a), i//2+1):
                ans = 1
                break
 
            if run_triplet(sorted(b), i//2+1):
                ans = 2
                break
 
    print(f'#{tc} {ans}')