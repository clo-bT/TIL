T = int(input()) #2
for tc in range(1,T+1):
    arr = [list(input()) for _ in range(5)]

    leng = 0    # 제일 긴 문자열 길이
    for i in arr:
        if leng < len(i):
            leng = len(i)
    # 긴걸로 다 맞춰
    for i in range(5):
        if len(arr[i]) < leng:
            arr[i] += ' ' * (leng-len(arr[i]))

    ans = ''
    for i in range(leng):
        for j in range(len(arr)):
            if arr[j][i] != ' ':
                ans += arr[j][i]
    
    print(f'#{tc}',ans)