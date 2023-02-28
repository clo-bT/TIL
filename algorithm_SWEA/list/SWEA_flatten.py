for tc in range(10):
    dump = int(input()) #834
    arr = list(map(int,input().split()))
    maxV = arr[0]
    minV = arr[0]

    # for i in range(len(arr)):
    #     if maxV < arr[i]:
    #         maxV = arr[i]
    #     if minV > arr[i]:
    #         minV = arr[i]
    while dump > 0 or maxV-minV != 1 or maxV - minV != 0:
        for i in range(len(arr)):
            if maxV < arr[i]:
                maxV = arr[i]
                maxVidx = i
            if minV > arr[i]:
                minV = arr[i]
                minVidx = i
        arr[maxVidx] -= 1
        arr[minVidx] += 1
        dump -= 1
    print(f'#{tc+1} {maxV-minV}') 

# 제일 높은 거 찾고 제일 낮은 거 찾아서 높은거 - 1 낮은거 + 1
# dump 횟수가 남아있을 때 종료, 높은 거 낮은 거 1 차이날 때 종료,
# 높은 거 낮은 거가 같을 때 종료



    