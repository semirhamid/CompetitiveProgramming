class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        else:
            hd = self.head
            for i in range(index ):
                hd = hd.next
            return hd.val

    def addAtHead(self, val: int) -> None:
        first = Node(val)
        if(self.head is not None):
            first.next = self.head
            self.head = first
        else:
            self.head = first
            self.tail = first
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if(self.head is None):
            self.addAtHead(val)
        else:
            last = Node(val)
            self.tail.next = last
            self.tail = last
            self.length += 1
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.length and index >= 0:
            if index == 0:
                self.addAtHead(val)
            elif index == self.length:
                self.addAtTail(val)
            else:
                temp = self.head
                for i in range(index - 1):
                    temp = temp.next
                nd = Node(val)
                nd.next = temp.next
                temp.next = nd
                self.length += 1
                

    def deleteAtIndex(self, index: int) -> None:
        if (self.head is not None and index >= 0 and index < self.length):
            if (index == 0):
                self.head = self.head.next
                if self.length == 1:
                    self.tail = None
            elif(index == self.length - 1):
                temp = self.head
                for i in range(index - 1):
                    temp = temp.next
                temp.next = None
                self.tail = temp
            else:
                temp = self.head
                for i in range(index - 1):
                    temp = temp.next
                temp.next = temp.next.next
            self.length -= 1
            
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
