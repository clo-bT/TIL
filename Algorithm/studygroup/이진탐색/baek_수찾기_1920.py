import sys
input = sys.stdin.readline

N = int(input()) #5
A = list(map(int,input().split())) #[4, 1, 5, 2, 3]
A.sort()
M = int(input()) #5
B = list(map(int,input().split())) #[1, 3, 7, 9, 5]

'''
for i in B:
    if i in A:
        print(1)
    else:
        print(0)
'''
def binary_search(i,li):
    s = 0                   # 왼쪽 커서
    e = len(li) - 1         # 오른쪽 커서
    while s <= e:           
        mid = (s+e) // 2    # 가운데
        if li[mid] == i:
            return 1
        elif li[mid] < i:
            s = mid + 1
        else:
            e = mid - 1
    return 0

for i in B:
    print(binary_search(i,A))
    