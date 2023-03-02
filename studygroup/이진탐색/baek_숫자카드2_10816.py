import sys
input = sys.stdin.readline

N = int(input()) #10
A = sorted(list(map(int,input().split()))) #[-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
M = int(input()) #8
B = list(map(int,input().split())) #[10, 9, -5, 2, 3, 4, 5, -10]

def binary_search(i, li):
    s = 0
    e = N - 1
    while s<=e:
        mid = (s + e) // 2
        if li[mid] == i:
            return li[s:e+1].count(i)
        elif li[mid] < i:
            s = mid + 1
        else:
            e = mid - 1
    return 0
    
for i in B:
    print(binary_search(i,A), end=' ')






'''
    while True:
        mid = (s + e) // 2
        if s > e:          # 종료조건
            return cnt
        if li[mid] == i:
            cnt += 1
            if li[mid+1] == i:
                if (e - s) % 2 == 1:
                    s += 1
            elif li[mid-1] == i:
                if (e - s) % 2 == 1:
                    e -= 1
            else:
                return cnt
            s += 1
            e -= 1
        elif li[mid] < i:
            s = mid + 1
        else:
            e = mid - 1
    for i in B:
    print(binary_search(i,A), end=' ')
'''