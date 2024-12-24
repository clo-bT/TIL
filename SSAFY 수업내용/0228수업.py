'''

# 비트 연산 예제1
def Bbit_print(i):
	output = ""
	for j in range(7, -1, -1):
			output += "1" if i & (1 << j) else "0"
	print(output)

for i in range(-5, 6):
	print("%3d = " % i, end='')
	Bbit_print(i)



#비트 연산 예제2
def Bbit_print(i):
	output = ""
	for j in range(7, -1, -1):
			output += "1" if i & (1 << j) else "0"
	print(output)
a = 0x10
x = 0x01020304
print("%d = " % a, end = '')
Bbit_print(a)
print()
print("0%X = " % x, end = '')
for i in range(0,4):
    Bbit_print((x >> i*8) & 0xff)


# 비트 연산 예제3

def ce(n):
    p = []
    for i in range(0,4):
        p.append((n>>(24 - i*8)) & 0xff)
    return p 

x = 0x01020304
p = []
for i in range(0,4):
    p.append((x>>(i*8)) & 0xff)



#비트 연산 예제4
def ce1(n):
    return (n<<24&0xff000000) | (n<<8&0xff000000) |(n>>8&0xff00) |(n>>24&0xff)


# 연습문제 3
arr = list(map(int,input()))
N = len(arr)
num = 0
for i in range(N):
    j = i % 7
    num += arr[i] * (2**(6-j))
    if j == 6:      #일곱자리 끊은 거. 7개 끊기
        print(num, end = '')
        num = 0

'''

# 16진수 -> 2진수
sixteen = input()
for x in sixteen:
    num = int(x, 16)
    for j in range(3, -1, -1):
        bit = 1 if num&(1<<j) else 0 
        print(bit, end = '')
    print('', end = '')

    
