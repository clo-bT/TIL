'''
class collatz():
    count = 0
    def __init__(self,num):
        self.num = num
        

        # 입력한 수가 짝수면 2로 나눠
    def cal(self):
        if int(self.num) % 2 == 0:
            self.num /= 2
            collatz.count += 1

        elif int(self.num) % 2 == 1:
            self.num = self.num * 3 + 1
            collatz.count += 1

        elif int(self.num) == 1:
            print(collatz.count)

        if collatz.count == 500:
            print(-1)

    pass
'''
class collatz():
    def __init__(self, num):
        count = 0
        self.num = num
        while self.num != 1:
            if self.num % 2 == 0:
                self.num = self.num / 2
                count += 1

            elif self.num % 2 == 1:
                self.num = self.num * 3 + 1
                count += 1

            if count >= 500:
                count = -1
                break

        print(count)


collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
