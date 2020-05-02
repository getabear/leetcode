class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        self.length=0
        self.stack2=[]
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack:
            self.stack2.append(self.stack.pop())
        self.stack.append(x)
        while self.stack2:
            self.stack.append(self.stack2.pop())
        self.length+=1



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.length>=1:
            self.length-=1
            return self.stack.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length==0