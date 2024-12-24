for _ in range(1, 11):
    sub = 1
    tc = int(input())
    arr = list(map(int,input().split()))
    while True:
        a = arr.pop(0)
        a -= sub
        arr.append(a)
        if sub != 5:
            sub += 1
        else:
            sub = 1
        if arr[-1] <= 0:
            arr[-1] = 0
            break
    print(arr)



'''
순환큐 이용한 교수님 코드
T = 10
for _ in range(T):
    tc = int(input())
    arr = [0] + list(map(int, input().split())) # 순환큐에 가득찬 형태로 초기화
    qsize = 9
    front = 0
    rear = 8
    i = 1
    while arr[rear] > 0:    # 맨 뒤에 인큐한 값이 0보다 크면
        front = (front + 1) % qsize
        tmp = arr[front]
        tmp -= i
        if tmp<0:
            tmp = 0
        rear = (rear + 1) % qsize
        arr[rear] = tmp
        i += 1
        if i==6:
            i = 1
    print(f'#{tc}', end = ' ')
    while front != rear:        # 큐에 숫자가 남아있으면
        front = (front + 1) % qsize
        print(arr[front], end = ' ')
    print()
'''