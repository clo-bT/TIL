
T = int(input()) #3
for tc in range(1, T+1):
    a, n = input().split()
    arr = list(map(int,a))
    for _ in range(int(n)):
        li = arr
        check = []
        while True:
            if not li:
                break
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    arr[i], arr[j] = arr[j], arr[i]
                    check.append(arr)
                    arr[i], arr[j] = arr[j], arr[i]
        check = set(check)
        n = list(check)
    check = list(map(int,check))
    print(f'{tc} {max(li)}')
'''
# 민웅님 코드
 
T = int(input())
 
for tc in range(1, T+1):
    num_pad, c = map(int, input().split())
    num = []
    num.append(str(num_pad))
    
    for _ in range(c):
        s_li = num
        check = []
        
        while True:
            if not s_li:
                break
            s = list(s_li.pop()) #['1', '2', '3']
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    s[i], s[j] = s[j], s[i]
                    check.append(''.join(s))
                    s[i], s[j] = s[j], s[i]
                    print(s)
        check = set(check) #dict
        num = list(check) #list
        
 
    check = list(map(int, check))
 
    print(f'#{tc} {max(check)}')
'''