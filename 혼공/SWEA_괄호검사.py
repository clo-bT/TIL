T = int(input()) #3

for tc in range(1, T+1):
    stack = []
    a = input() #print('{} {}'.format(1, 2))
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        elif i == '{':
            stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append('}')
    if len(stack) == 0:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)
