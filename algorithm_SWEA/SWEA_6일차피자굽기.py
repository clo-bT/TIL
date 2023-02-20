# 교수님 코드
T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 5 
    pizza = list(map(int,input().split())) #7 2 6 5 3
    oven = []

    # 화덕 채우기
    for i in range(N):
        oven.append(pizza[i]) # 피자번호
    last = N - 1            # 화덕에 들어간 마지막 피자번호
    # 더이상 피자가 없을 때까지 회전
    ans = 0                 # 마지막으로 완성된 피자번호
    while oven:
        num = oven.pop(0)   # 입구로 돌아온 피자번호
        pizza[num] //= 2    # 한바퀴 돌면서 절반이 녹음
        if pizza[num] > 0 : # 완전히 녹지 않은 경우
            oven.append(num)
        else:
            ans = num       # 이후에 나오는 피자가 없으면 마지막 피자
            if last + 1 < M:# 아직 화덕에 들어가지 않은 피자가 있으면
                last += 1   # 추가로 화덕에 투입
                oven.append(last) 
    print(f'#{tc}',ans+1)









'''
채련님 코드
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    Ci = list(map(int, input().split()))
 
    # 피자 등번호 달아주기
    for i in range(1, M+1):
        Ci[i-1] = [i, Ci[i-1]]
 
    cnt = 0
    queue = [Ci.pop(0) for _ in range(N)]
    last_pizza = []
 
    while True:
        if len(queue) == 1:
            last_pizza = queue[0]
            break
        item = queue.pop(0) # 맨 앞 피자 빼서
        if item[1] // 2 > 0: # 피자시간을 2로 나눈게 0보다 크면 더돌려야한다
            item = [item[0], item[1]//2]
            queue.append(item) # 더돌려야되니까 화덕에 추가해준다
        else: # 나눴는데 0이면 빼고 새로운 핏짜 추가
            if len(Ci) > 0: # 피자가 남았는지 확인하고
                queue.append(Ci.pop(0)) # 핏짜 추가
 
    print(f'#{tc} {last_pizza[0]}')
'''
'''
재영님 코드
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
 
    tmp = list(map(int, input().split()))
 
    pizza_lst = [[(i + 1), tmp[i]] for i in range(M)]   # [피자 번호, 피자 치즈]
 
    fire = [pizza_lst.pop(0) for _ in range(N)]
 
    while len(fire) > 1:        # 화덕에 피자가 하나만 남을 때까지
        fire[0][1] //= 2        # 치즈 녹은 것 확인
        if fire[0][1] == 0:     # 치즈 다 녹으면 피자 빼기
            fire.pop(0)
            if pizza_lst:       # 남은 피자 있으면
                fire.append(pizza_lst.pop(0))   # 화덕에 집어넣기
        else:                   # 치즈 다 안 녹았으면 회전
            fire.append(fire.pop(0))
 
    print(f'#{tc} {fire[0][0]}')    # 피자 번호 출력
'''


