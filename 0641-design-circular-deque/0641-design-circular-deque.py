class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = -1
        self.rear = - 1
        self.size = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.size == 0:
            self.front = self.rear = 0
            self.queue[self.front] = value
            self.size += 1
            return True

        if self.queue[(self.front-1)%self.k] is not None:
            return False
        self.front = (self.front -1)%self.k
        self.queue[self.front] = value
        self.size += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.size == 0:
            self.front = self.rear = 0
            self.queue[self.front] = value
            self.size += 1
            return True
        if self.queue[(self.rear + 1)%self.k] is not None:
            return False
        self.rear = (self.rear + 1)%self.k
        self.queue[(self.rear )%self.k] = value
        self.size += 1
        return True
    def deleteFront(self) -> bool:
        if self.queue[self.front] is None:
            return False
        self.queue[self.front] = None
        self.front = (self.front +1)%self.k
        self.size -=1
        if self.size == 0:
            self.front = self.rear =-1
        return True
    def deleteLast(self) -> bool:
        if self.queue[self.rear] is None:
            return False
        self.queue[self.rear] = None
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = -1
        return True
    def getFront(self) -> int:
        return self.queue[self.front] if self.queue[self.front] is not None else -1 
    def getRear(self) -> int:
        return self.queue[self.rear] if self.queue[self.rear] is not None else -1 
    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()