'''
# 이게뭘까

n = int(input())
def fibo(n):
    f,g = fibo(n//2)
    if n % 2 == 0:
        return (f^2 + g^2 + fibo(f+g))

print(fibo(n))

'''
'''
# 구글링_메모이제이션
from sys import stdin

def fibo(n,l):
    if n < 2:
        return n 
    if l[n] == 0:
        l[n] = fibo(n-1,l) + fibo(n-2,l)
    return l[n]
def fib_help(n):
    return fibo(n, [0 for _ in range(n+1)])
n = int(stdin.readline())
print(fib_help(n) % 1000000)

# 997까지는 구해짐
'''


# 구글링_동적계획법
from sys import stdin
def fibo(n):
    li = [0,1]
    if n < 2:
        return li[n]
    else:
        for i in range(2, n+1):
            li.append(li[i-1] + li[i-2])
        return li[n]
print(fibo(int(stdin.readline())) % 1000000)


