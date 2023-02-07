t = int(input()) #9
for tc in range(t):
    a,b,c = map(int,input().split()) # 5 2 6
    if a > b > c or c > b > a:
        print(b)
    elif b > a > c or c > a > b:
        print(a)
    elif b > c > a or a > c > b:
        print(c)
