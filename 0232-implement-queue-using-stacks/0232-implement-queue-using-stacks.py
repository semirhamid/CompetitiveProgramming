class MyQueue:

    def __init__(self):
        self.q1 = []

    def push(self, x) :
        self.q1.append(x)

    def pop(self):
        q2 = []
        for i in range(len(self.q1)):
            q2.append(self.q1[-1-i])
        self.q1=[]
        temp = q2.pop()
        for i in range(len(q2)):
            self.q1.append(q2[-1-i])
        return temp

    def peek(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()