class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min_stack=[]   #用以记录最小的值

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack)==0 or x<=self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        x=self.stack.pop()
        if self.min_stack and x==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]