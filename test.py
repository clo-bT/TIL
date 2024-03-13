import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    cnt = 0
    arr = list(map(float,input().split()))
    avg = sum(arr[1:])/arr[0]
    # print(avg)
    for i in range(1,len(arr)):
        if arr[i] > avg:
            cnt += 1
    print(str(round((cnt/arr[0])*100,3))+'%')
    
