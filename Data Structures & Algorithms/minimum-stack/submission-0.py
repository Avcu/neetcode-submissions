class MinStack:

    def __init__(self):
        self.stackList = []
        self.minStackList = []   # will store the min that has seen for far

    def push(self, val: int) -> None:
        self.stackList.append(val)
        if self.minStackList:
            lastMin = self.minStackList[-1]
            self.minStackList.append(min(lastMin, val))
        else:
            self.minStackList.append(val)

    def pop(self) -> None:
        self.stackList.pop()
        self.minStackList.pop()

    def top(self) -> int:
        return self.stackList[-1]

    def getMin(self) -> int:
        return self.minStackList[-1]
        
