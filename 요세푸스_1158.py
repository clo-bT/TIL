N, K = map(int,input().split()) #7, 3

li = []
new = []

for i in range(1, N + 1): # 1부터 8까지
    li.append(i) # li = [1,2,3,4,5,6,7]
k = K-1
for _ in range(N): # 7번 pop
    k = k % len(li)
    kpop = li.pop(k)
    new.append(kpop)
    k += 2

result = ','.join(map(str,new))
print(f'<{result}>')

'''
[1,2,3,4,5,6,7] (3) k = 2
[1,2,4,5,6,7] (6) k = 4
[1,2,4,5,7] (2) k = 6 , k = 1
[1,4,5,7] (7) k = 3
[1,4,5] (5) k = 5 k = 2
[1,4](1) k = 4
'''

'''
for i in range(1, N + 1):
    li.append(i) # [1,2,3,4,5,6,7]

for _ in range(N):
    kpop = li.pop(K-1) # K-1 = 2 
    K += 2 # k = 5
    print(kpop)
    if K-1 >= len(li):
        K = K % (len(li)+1)

    new.append(kpop)
print(new)
'''