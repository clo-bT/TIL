'''
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = int(input()) #5
for tc in range(t):
    n = int(input()) #1
    s = input() #a
    li = []
    
    for i in range(1, len(alpa)+1):
        for j in range(n):
            if alpa[i] == s[j]:
                li.append(i)
                maxV = li[0] # 얘 어디다가 써야할지 모름
            for k in range(len(li)):
                if maxV < li[k]:
                    maxV = li[k]


codeforces
3 15 4 5 6 15 18 3 5 19
'''