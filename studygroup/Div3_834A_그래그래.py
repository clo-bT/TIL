T = int(input()) #12
word = 'Yes'*30
for tc in range(1,T+1):
    a = input()
    if a in word:
        print("YES")
    else:
        print("NO")