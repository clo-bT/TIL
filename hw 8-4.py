class Stack():
    def __init__(self):
        self.stack = []
        

    def empty(cls):
        if len(cls.stack) == 0:
            return True
        else:
            return False

    def top(cls):
        return cls.stack[-1]

    def pop(cls):
        if len(cls.stack) == 0:
            return None
        else:
            po = cls.stack.pop(-1)
            return po

    def push(cls, a):
        cls.stack.append(a)
        

    def __repr__(self):
        return self.stack


s1 = Stack()
print(s1.empty()) #True
s1.push(1) 
s1.push(3)
s1.push(2)
print(s1.top()) #2
print(s1.__repr__()) #[1, 3, 2]
print(s1.pop()) #2
print(s1.__repr__()) #[1,3]
