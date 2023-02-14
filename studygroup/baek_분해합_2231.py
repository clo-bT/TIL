N = int(input()) #216
sum_a = 0
li = []
for a in range(1, N+1):
    A = list(map(int,str(a))) #[2,1,6]
    sum_a = a + sum(A)
    if sum_a == N:
        li.append(a)
if len(li) == 0:
    print(0)
else:
    print(min(li))
    

    