class CQueue1:
    # 3148ms
    def __init__(self):
        self.stack=[]
        self.queue=[]

    def appendTail(self, value: int) -> None:
        while self.queue:
            self.stack.append(self.queue.pop())
        self.queue.append(value)
        while self.stack:
            self.queue.append(self.stack.pop())

    def deleteHead(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop()

class CQueue:

    def __init__(self):
        self.stack=[]
        self.queue=[]

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if not self.queue:
            while self.stack:
                self.queue.append(self.stack.pop())
            if not self.queue:
                return -1
        return self.queue.pop()
