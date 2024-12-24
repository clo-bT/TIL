def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data
    
def dequeue():
    global front
    front += 1
    return queue[front]


queue = [0] * 10
front = -1
rear = -1

from collections import deque

q1 = deque()
q1.append(100)
q1.append(300)
q1.append(200)
print(q1.popleft)
print(q1.popleft)
print(q1.popleft)